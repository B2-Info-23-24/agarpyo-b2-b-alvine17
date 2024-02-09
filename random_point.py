import pygame
import random  

class Point:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 7
        self.color = (0, 255, 0)  
        self.position = pygame.Vector2(random.randint(0, self.screen_width), random.randint(0, self.screen_height))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
