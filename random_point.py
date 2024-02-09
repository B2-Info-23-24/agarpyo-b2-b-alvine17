import pygame
import random  

class Point:
    def __init__(self, s_width, s_height):
        self.s_width = s_width
        self.s_height = s_height
        self.radius = 7
        self.color = (0, 255, 0)  
        self.position = pygame.Vector2(random.randint(0, self.s_width), random.randint(0, self.s_height))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
