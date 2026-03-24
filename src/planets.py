from Planet import Planet
from Sun import Sun
import math

SCALE = 0.1
G = 1
M = 1000

sun = Sun(M, (200, 200))
merkurius_distance = 10
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
    )
]
