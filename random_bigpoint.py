import pygame 
import random

class BigPoint:
    def __init__(self, s_width, s_height, nb_point=3, radius=20):
        self.s_width = s_width
        self.s_height = s_height
        self.nb_point = nb_point
        self.radius = radius
        self.points = []

        self.spawn_points()

    def spawn_points(self):
        self.points = []
        for _ in range(self.nb_point):
            point = self.pos_point_random()
            self.points.append(point)

    def pos_point_random(self):
        x = random.randint(0, self.s_width)
        y = random.randint(0, self.s_height)
        return pygame.Vector2(x, y)

    def point_collition(self, player_radius, player_pos):
        for point in self.points:
            distance = point.distance_to(player_pos)
            if distance < self.radius + player_radius:
                if player_radius > self.radius:
                    times_larger = player_radius // self.radius
                    player_radius //= times_larger
                    player_pos.x //= times_larger
                    player_pos.y //= times_larger
                else:
                    pass

    def draw(self, screen):
        for point in self.points:
            pygame.draw.circle(screen, (255, 0, 0), (int(point.x), int(point.y)), self.radius)
