import math
from Sun import Sun


class Planet:
    def __init__(
        self,
        mass: float | None,
        coords: tuple[int, int],
        star: Sun,
        velocity: tuple[float, float],
        id: str | int,
        scale: float,
        G: int,
        color: tuple[int, int, int] = (0, 255, 0),
    ):
        self.mass = mass
        self.coords = coords
        self.star = star
        self.velocity = velocity
        self.id = id
        self.closest_neighbor_counts: dict[Planet, int] = {}
        self.scale = scale
        self.G = G
        self.color = color

    def __repr__(self) -> str:
        return f"Planet {self.id}"

    def update_coords(self):
        self.calculate_v()
        self.coords = (
            self.coords[0] + self.velocity[0],
            self.coords[1] + self.velocity[1],
        )

    def update_closest_neighbors(self, neighbor):
        if neighbor in self.closest_neighbor_counts:
            self.closest_neighbor_counts[neighbor] += 1
        else:
            self.closest_neighbor_counts[neighbor] = 1

    def get_closest_neighbor_coords(self):
        # Function should not be called if there has not been neighbors added
        if len(self.closest_neighbor_counts) == 0:
            raise ValueError(f"Planet '{self.id}' has no recorded neighbors.")
        else:
            sorted_dist_list = sorted(
                self.closest_neighbor_counts.items(), key=lambda x: x[1], reverse=True
            )
            return sorted_dist_list[0][0].coords

    def calculate_v(self):
        dx = self.star.coords[0] - self.coords[0]
        dy = self.star.coords[1] - self.coords[1]

        # R is the distance
        R = math.sqrt(dx**2 + dy**2)

        # Avoid division by zero if planet is inside the star
        if R < 1:
            R = 1

        # atan2(y, x) handles all quadrants and dx=0 cases
        theta = math.atan2(dy, dx)

        # Gravity formula: GM / R^2
        accel = (self.G * self.star.mass / (R**2)) * self.scale

        # Update velocity
        new_vx = self.velocity[0] + math.cos(theta) * accel
        new_vy = self.velocity[1] + math.sin(theta) * accel

        self.velocity = (new_vx, new_vy)
