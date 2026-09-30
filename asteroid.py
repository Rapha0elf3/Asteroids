import pygame
from logger import log_state, log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) ->  None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        vector_plus = self.velocity.rotate(new_angle)
        vector_minus = self.velocity.rotate(new_angle * (-1))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_plus = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_plus.velocity = vector_plus * 1.2
        split_asteroid_minus = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_minus.velocity = vector_minus * 1.2
