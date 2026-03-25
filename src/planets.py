from .Planet import Planet
from .Sun import Sun
import math

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
planets = [
    Planet(
        mass=10,
        coords=(200, sun.coords[1] - merkurius_distance),
        star=sun,
        velocity=(math.sqrt(G * M * SPEED_SCALE / (merkurius_distance)), 0),
        id="Mercury",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(100, 100, 100),
    ),
    Planet(
        mass=8.15,  # Relative to Mercury's mass scale
        coords=(200, int(sun.coords[1] + venus_dist)),
        star=sun,
        velocity=(-math.sqrt(G * M * SPEED_SCALE / venus_dist), 0),
        id="Venus",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(255, 198, 73),
    ),
    Planet(
        mass=10.0,
        coords=(200, int(sun.coords[1] - earth_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SPEED_SCALE / earth_dist), 0),
        id="Earth",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(100, 149, 237),
    ),
    Planet(
        mass=1.07,
        coords=(200, int(sun.coords[1] + mars_dist)),
        star=sun,
        velocity=(-math.sqrt(G * M * SPEED_SCALE / mars_dist), 0),
        id="Mars",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(193, 68, 14),
    ),
    Planet(
        mass=3178,  # Jupiter is ~318x Earth mass
        coords=(200, int(sun.coords[1] - jupiter_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SPEED_SCALE / jupiter_dist), 0),
        id="Jupiter",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(216, 202, 157),
    ),
    Planet(
        mass=951,
        coords=(200, int(sun.coords[1] + saturn_dist)),
        star=sun,
        velocity=(-math.sqrt(G * M * SPEED_SCALE / saturn_dist), 0),
        id="Saturn",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(225, 198, 110),
    ),
    Planet(
        mass=145,
        coords=(200, int(sun.coords[1] - uranus_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SPEED_SCALE / uranus_dist), 0),
        id="Uranus",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(209, 231, 231),
    ),
    Planet(
        mass=171,
        coords=(200, int(sun.coords[1] + neptune_dist)),
        star=sun,
        velocity=(-math.sqrt(G * M * SPEED_SCALE / neptune_dist), 0),
        id="Neptune",
        speed_scale=SPEED_SCALE,
        G=G,
        color=(63, 115, 255),
    ),
]
