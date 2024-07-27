import random
import pygame

# Draws a circle that falls from wherever it is created.
# Can be given an initial speed in any direction.
# Each frame the y speed will slowly shift by the GRAVITY amount


class Particle:
    GRAVITY = 0.1  # changes the rate that particles move towards bottom of screen
    WEIGHT_MAX = 20  # affects size and wind resistance

    def __init__(self, window: pygame.surface, windowWidth: int, windowHeight: int, loc: tuple, speed: tuple,
                 color: tuple = (255, 255, 255), weight=None):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        if weight is None:
            self.weight = random.randrange(1, Particle.WEIGHT_MAX + 1)
        else:
            self.weight = weight

        self.x = loc[0]
        self.y = loc[1]
        self.speedX = speed[0]
        self.speedY = speed[1]

        self.dead = False
        self.color = color
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    def update(self):
        self.speedY += Particle.GRAVITY
        self.x += self.speedX
        self.y += self.speedY

        if self.y > self.windowHeight:
            self.dead = True

    def draw(self):
        pygame.draw.circle(self.window, (self.r, self.g, self.b), (self.x, self.y), self.weight, 0)
