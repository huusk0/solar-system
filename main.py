import pygame
import math
from src.planets import planets as premade_planets
from src.Sun import Sun
import random


def randomize_planet_angles(planets, sun):
    for p in planets:
        dx = p.coords[0] - sun.coords[0]
        dy = p.coords[1] - sun.coords[1]

        r = math.sqrt(dx * dx + dy * dy)
        speed = math.sqrt(p.velocity[0] ** 2 + p.velocity[1] ** 2)

        angle = random.uniform(0, 2 * math.pi)

        # new position
        new_x = sun.coords[0] + r * math.cos(angle)
        new_y = sun.coords[1] + r * math.sin(angle)

        # tangential velocity
        vx = -math.sin(angle) * speed
        vy = math.cos(angle) * speed

        p.coords = (new_x, new_y)
        p.velocity = (vx, vy)


# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Drawing Window")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for buttons
font = pygame.font.SysFont(None, 24)

# Button rectangles
start_rect = pygame.Rect(50, 350, 100, 30)
quit_rect = pygame.Rect(250, 350, 100, 30)

sun = Sun(2000, (200, 200))

planets = premade_planets
inner_planets = set(planets[:4])
outer_planets = set(planets[4:])
# Main loop
running = True
screen.fill(black)

min_dist_planet_pairs = {}
start_coords = {p: p.coords for p in planets}
ticks = 0
moving = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if start_rect.collidepoint(mouse_x, mouse_y):
                moving = True
            elif quit_rect.collidepoint(mouse_x, mouse_y):
                running = False
    # Fill screen with white
    screen.fill(black)
    # Draw sun and planets
    pygame.draw.circle(screen, yellow, sun.coords, 5)

    # Draw alternative sun and planets
    sun2_coords = (sun.coords[0] + 400, sun.coords[1])
    pygame.draw.circle(screen, yellow, sun2_coords, 5)

    # Draw "distance scale" boundary
    pygame.draw.circle(screen, (100, 100, 100), sun.coords, 50, width=2)
    pygame.draw.circle(screen, (100, 100, 100), sun2_coords, 50, width=2)
    # Update planet position if moving
    if moving:
        # Dont update planet positions since we randomize them on each tick
        # for planet in planets:
        #     planet.update_coords()
        for i, planet in enumerate(planets):
            # 1. Draw the planet (ensure coords are ints)
            if i < 4:
                pos_i = (int(planet.coords[0]), int(planet.coords[1]))
                pygame.draw.circle(screen, planet.color, pos_i, 2)

                pos_i2 = (start_coords[planet][0] + 400, start_coords[planet][1])
                pygame.draw.circle(screen, planet.color, pos_i2, 2)
            else:
                dx = (sun.coords[0] - planet.coords[0]) * 0.4
                dy = (sun.coords[1] - planet.coords[1]) * 0.4

                dx_s = (sun.coords[0] - start_coords[planet][0]) * 0.4
                dy_s = (sun.coords[0] - start_coords[planet][1]) * 0.4

                pos_i = (int(sun.coords[0] - dx), int(sun.coords[1] - dy))
                pygame.draw.circle(screen, planet.color, pos_i, 2)

                pos_i2 = (int(sun.coords[0] - dx_s) + 400, int(sun.coords[1] - dy_s))
                pygame.draw.circle(screen, planet.color, pos_i2, 2)

            min_dist_sq = float("inf")
            min_planet = None

            # 2. Find nearest neighbor
            for j, neighbor in enumerate(planets):
                if i == j:
                    continue

                # Use squared distance to avoid expensive math.sqrt()
                dx = planet.coords[0] - neighbor.coords[0]
                dy = planet.coords[1] - neighbor.coords[1]
                dist_sq = dx**2 + dy**2

                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    min_planet = neighbor

            # 3. Draw the line
            if min_planet:
                # # Figure 1 closest neighbor atm
                # pos_j = (int(min_planet.coords[0]), int(min_planet.coords[1]))
                # pygame.draw.line(screen, red, pos_i, pos_j, 1)

                # Update neighbors
                planet.update_closest_neighbors(min_planet)

                # Figure 2 most closest neighbor
                pos_j2_temp = planet.get_closest_neighbor()

                if pos_j2_temp in inner_planets:
                    pos_j2 = (
                        int(start_coords[pos_j2_temp][0] + 400),
                        int(start_coords[pos_j2_temp][1]),
                    )
                    pygame.draw.line(screen, green, pos_i2, pos_j2, 1)
                else:
                    dx_s = (sun.coords[0] - start_coords[pos_j2_temp][0]) * 0.4
                    dy_s = (sun.coords[0] - start_coords[pos_j2_temp][1]) * 0.4
                    pos_j2 = (
                        int(sun.coords[0] - dx_s) + 400,
                        int(sun.coords[1] - dy_s),
                    )
                    pygame.draw.line(screen, green, pos_i2, pos_j2, 1)

                if (planet, min_planet) in min_dist_planet_pairs:
                    min_dist_planet_pairs[(planet, min_planet)] += 1
                elif (min_planet, planet) in min_dist_planet_pairs:
                    min_dist_planet_pairs[(min_planet, planet)] += 1
                else:
                    min_dist_planet_pairs[(planet, min_planet)] = 1

    # Draw buttons
    pygame.draw.rect(screen, white, start_rect, 2)
    pygame.draw.rect(screen, white, quit_rect, 2)

    # Render and draw button text
    start_text = font.render("Start", True, white)
    quit_text = font.render("Quit", True, white)
    screen.blit(start_text, (start_rect.x + 10, start_rect.y + 5))
    screen.blit(quit_text, (quit_rect.x + 10, quit_rect.y + 5))

    # Draw each planets neighborlist into the GUI
    if moving:
        for i, planet in enumerate(planets):
            max_planet = max(planet.closest_neighbor_counts.values())
            p_list = [i - max_planet for i in planet.closest_neighbor_counts.values()]
            # The standard Pythonic way for dictionaries
            p_map = {
                k: v - max_planet for k, v in planet.closest_neighbor_counts.items()
            }
            planets_text = font.render(
                f"{planet} => {p_map}",
                True,
                white,
            )
            screen.blit(planets_text, (10, 400 + 20 * i))
        tick_text = font.render(f"tick: {ticks}", True, white)
        screen.blit(tick_text, (10, 400 + 20 * (i + 1)))

    # Update display
    pygame.display.flip()
    ticks += 1
    if ticks % 1 == 0:
        randomize_planet_angles(planets, sun)
    # if ticks == 1000:
    #     print("RESULTS AFTER 1000:")
    #     for planet in planets:
    #         print(f"{planet.id} = {planet.closest_neighbor_counts}")
    #     print("###########")
    #     ticks = 0
    # Cap frame rate
    clock.tick(6000)

    # sorted_dist_list = sorted(
    #     min_dist_planet_pairs.items(), key=lambda x: x[1], reverse=True
    # )
    # if len(sorted_dist_list) != 0:
    #     print(sorted_dist_list)
    # print(planets[0].closest_neightbor_counts)

# Quit pygame
pygame.quit()
