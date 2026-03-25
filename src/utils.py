import math
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
