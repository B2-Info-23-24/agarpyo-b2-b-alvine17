import pygame
import random

class Point:
    def __init__(self, s_width, s_height, nb_food=5, food_radius=10, player_radius=40):
        self.s_width = s_width
        self.s_height = s_height
        self.food_radius = food_radius
        self.player_radius = player_radius
        self.food_list = []
        self.score = 0  
        self.speed = 100
        self.size = 40 

        self.eating(nb_food)

    def eating(self, nb_food):
        self.food_list = []
        for _ in range(nb_food):
            x = random.randint(0, self.s_width)
            y = random.randint(0, self.s_height)
            color = (0, 255, 0)  
            self.food_list.append({'position': pygame.Vector2(x, y), 'color': color})

    def collision(self, player_position):
        for index, food in enumerate(self.food_list):
            distance = food['position'].distance_to(player_position)
            if distance < self.food_radius + self.player_radius:
                self.player_radius += 1 
                self.score += 1 
                self.speed += 5
                self.size += 2
                return index
        return None

    def update_food_pos(self, index):
        if index is not None:
            x = random.randint(0, self.s_width)
            y = random.randint(0, self.s_height)
            color = (0, 255, 0)
            self.food_list[index] = {'position': pygame.Vector2(x, y), 'color': color}

    def draw(self, screen, player_pos):
        for food in self.food_list:
            pygame.draw.circle(screen, food['color'], (int(food['position'].x), int(food['position'].y)), self.food_radius)
            pygame.draw.circle(screen, "yellow", (int(player_pos.x), int(player_pos.y)), self.player_radius + self.player_radius)

    def get_score(self):  
        return f"Score: {self.score}"

    def get_speed(self):  
        return f"Vitesse: {self.speed}"

    def get_size_point(self): 
        return f"Taille: {self.size}"
    
    def reset(self):
        self.score = 0  
        self.speed = 100  
        self.size = 40  
        self.player_radius = 40