import pygame
import random

class BigPoint:
    def __init__(self, s_width, s_height, nb_point=2, min_radius=40, max_radius=150):
        self.s_width = s_width
        self.s_height = s_height
        self.nb_point = nb_point
        self.min_radius = min_radius
        self.max_radius = max_radius
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
        radius = random.randint(self.min_radius, self.max_radius)
        return pygame.Vector2(x, y), radius

    def point_collition(self, player_radius, player_pos):
        for point, radius in self.points:
            distance = point.distance_to(player_pos)
            if distance < radius + player_radius:
                if player_radius > radius:
                    times_larger = player_radius // radius
                    player_radius //= times_larger
                    player_pos.x //= times_larger
                    player_pos.y //= times_larger
                    player_radius -= radius
                    if player_radius < 0:
                        player_radius = 0  # Assurez-vous que le rayon du joueur ne devienne pas négatif
                else:
                    # Si le joueur est plus petit que la boule rouge, masquez le joueur
                    player_radius = 0

    def draw(self, screen):
        for point, radius in self.points:
            pygame.draw.circle(screen, (255, 0, 0), (int(point.x), int(point.y)), radius)
