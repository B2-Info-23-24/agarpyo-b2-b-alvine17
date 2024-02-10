import pygame 
import random

class BigPoint:
    def __init__(self, s_width, s_height, nb_point=3, radius=20):
        self.s_width = s_width
        self.s_height = s_height
        self.nb_point = nb_point
        self.radius = radius
        self.points = []

        for _ in range(nb_point):
            point = self.pos_point_random()
            self.points.append(point)

    def pos_point_random(self):
        x = random.randint(0, self.s_width)
        y = random.randint(0, self.s_height)
        return pygame.Vector2(x, y)

    def draw(self, screen):
        for point in self.points:
             pygame.draw.circle(screen, (255, 0, 0), (int(point.x), int(point.y)), self.radius)
