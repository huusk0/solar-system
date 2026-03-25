from .Planet import Planet
from .Sun import Sun
import math
import random  # Added for randomness

SPEED_SCALE = 0.005
G = 1
M = 1000

sun = Sun(M, (200, 200))
merkurius_distance = 10
venus_dist = 18.6
earth_dist = 25.8
mars_dist = 39.3
jupiter_dist = 134.4
saturn_dist = 246.5
uranus_dist = 495.6
neptune_dist = 776.7


# Helper function to generate random starting position and velocity
def random_planet_setup(distance, sun_coords, g, m, speed_scale):
    # 1. Keep x and y as ints as requested
    angle = random.uniform(0, 2 * math.pi)
    x = int(sun_coords[0] + distance * math.cos(angle))
    y = int(sun_coords[1] + distance * math.sin(angle))
    coords = (x, y)

    # 2. Calculate actual distance from the resulting ints
    dx = x - sun_coords[0]
    dy = y - sun_coords[1]
    dist = math.sqrt(dx**2 + dy**2)

    # 3. Corrected Tangential Velocity
    # mag must be (sqrt(GM/r) * speed_scale) to match your accel scaling
    mag = math.sqrt((g * m * SPEED_SCALE) / dist)

    # Perpendicular vector to (dx, dy) is (-dy, dx)
    vx = -dy / dist * mag
    vy = dx / dist * mag
    velocity = (vx, vy)

    return coords, velocity


merkurius_coords, merkurius_velocity = random_planet_setup(
    merkurius_distance, sun.coords, G, M, SPEED_SCALE
)
venus_coords, venus_velocity = random_planet_setup(
    venus_dist, sun.coords, G, M, SPEED_SCALE
)
earth_coords, earth_velocity = random_planet_setup(
    earth_dist, sun.coords, G, M, SPEED_SCALE
)
mars_coords, mars_velocity = random_planet_setup(
    mars_dist, sun.coords, G, M, SPEED_SCALE
)
jupiter_coords, jupiter_velocity = random_planet_setup(
    jupiter_dist, sun.coords, G, M, SPEED_SCALE
)
saturn_coords, saturn_velocity = random_planet_setup(
    saturn_dist, sun.coords, G, M, SPEED_SCALE
)
uranus_coords, uranus_velocity = random_planet_setup(
    uranus_dist, sun.coords, G, M, SPEED_SCALE
)
neptune_coords, neptune_velocity = random_planet_setup(
    neptune_dist, sun.coords, G, M, SPEED_SCALE
)

planets = [
    Planet(
        mass=10,
        coords=merkurius_coords,
        star=sun,
        velocity=merkurius_velocity,
        id="Mercury",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(100, 100, 100),
    ),
    Planet(
        mass=8.15,
        coords=venus_coords,
        star=sun,
        velocity=venus_velocity,
        id="Venus",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(255, 198, 73),
    ),
    Planet(
        mass=10.0,
        coords=earth_coords,
        star=sun,
        velocity=earth_velocity,
        id="Earth",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(100, 149, 237),
    ),
    Planet(
        mass=1.07,
        coords=mars_coords,
        star=sun,
        velocity=mars_velocity,
        id="Mars",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(193, 68, 14),
    ),
    Planet(
        mass=3178,
        coords=jupiter_coords,
        star=sun,
        velocity=jupiter_velocity,
        id="Jupiter",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(216, 202, 157),
    ),
    Planet(
        mass=951,
        coords=saturn_coords,
        star=sun,
        velocity=saturn_velocity,
        id="Saturn",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(225, 198, 110),
    ),
    Planet(
        mass=145,
        coords=uranus_coords,
        star=sun,
        velocity=uranus_velocity,
        id="Uranus",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(209, 231, 231),
    ),
    Planet(
        mass=171,
        coords=neptune_coords,
        star=sun,
        velocity=neptune_velocity,
        id="Neptune",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(63, 115, 255),
    ),
]
