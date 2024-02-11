import pygame
from menu import main_menu
from random_point import Point  
from random_bigpoint import BigPoint

pygame.init()
pygame.display.set_caption("Jeu")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
points = []
player_radius = 20



big_point = BigPoint(screen.get_width(), screen.get_height())


points.append(Point(screen.get_width(), screen.get_height())) 

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mouse_pressed = False 

font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if pygame.Vector2(event.pos).distance_to(player_pos) <= 40:
                    mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pressed = False

    big_point.point_collition(player_radius, player_pos)

    index = points[0].collision(player_pos)  
    if index is not None:
        points[0].update_food_pos(index)

    if mouse_pressed:
        player_pos = pygame.mouse.get_pos()

    if player_pos.x < 0:
        player_pos.x = screen.get_width()
    elif player_pos.x > screen.get_width():
        player_pos.x = 0
    if player_pos.y < 0:
        player_pos.y = screen.get_height()
    elif player_pos.y > screen.get_height():
        player_pos.y = 0


    screen.fill("black")
    pygame.draw.circle(screen, "yellow", player_pos, 40)
    big_point.draw(screen)
    for point in points:
        point.draw(screen, player_pos)


    score_text = font.render(points[0].get_score(), True, (255, 255, 255))
    speed_text = font.render(points[0].get_speed(), True, (255, 255, 255))
    size_text = font.render(points[0].get_size_point(), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 50))
    screen.blit(size_text, (10, 90))
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

    player_radius = 20

points[0].reset()

pygame.quit()
