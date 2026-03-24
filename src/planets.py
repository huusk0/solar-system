from Planet import Planet
from Sun import Sun
import math

SCALE = 0.1
G = 1
M = 1000

sun = Sun(M, (200, 200))
merkurius_distance = 10
venus_dist = 18.6
earth_dist = 25.8
mars_dist = 39.3

planets = [
    Planet(
        mass=10,
        coords=(200, sun.coords[1] - merkurius_distance),
        star=sun,
        velocity=(math.sqrt(G * M * SCALE / (merkurius_distance)), 0),
        id="Mercury",
        scale=SCALE,
        G=G,
        color=(100, 100, 100),
    ),
    Planet(
        mass=8.15,  # Relative to Mercury's mass scale
        coords=(200, int(sun.coords[1] - venus_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SCALE / venus_dist), 0),
        id="Venus",
        scale=SCALE,
        G=G,
        color=(255, 198, 73),
    ),
    Planet(
        mass=10.0,
        coords=(200, int(sun.coords[1] - earth_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SCALE / earth_dist), 0),
        id="Earth",
        scale=SCALE,
        G=G,
        color=(100, 149, 237),
    ),
    Planet(
        mass=1.07,
        coords=(200, int(sun.coords[1] - mars_dist)),
        star=sun,
        velocity=(math.sqrt(G * M * SCALE / mars_dist), 0),
        id="Mars",
        scale=SCALE,
        G=G,
        color=(193, 68, 14),
    ),
]
