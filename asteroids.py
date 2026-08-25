import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_asteroid_vector1 = self.velocity.rotate(angle)
        new_asteroid_vector2 = self.velocity.rotate(-angle)
        new_asteroidradius1 = self.radius - ASTEROID_MIN_RADIUS
        new_asteroidradius2 = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroidradius1)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroidradius2)
        new_asteroid1.velocity = new_asteroid_vector1 * 1.2
        new_asteroid2.velocity = new_asteroid_vector2 * 1.2
