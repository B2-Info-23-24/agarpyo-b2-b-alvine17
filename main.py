import pygame
from end_menu import GameOverMenu
from menu import main_menu
from random_point import Point  
from random_bigpoint import BigPoint

pygame.init()
pygame.display.set_caption("Jeu")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_radius = 20

game_over_menu = None

big_point = BigPoint(screen.get_width(), screen.get_height())
points = [Point(screen.get_width(), screen.get_height())]  

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mouse_pressed = False 

font = pygame.font.Font(None, 36)

start_time = pygame.time.get_ticks()
total_time = 60

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: 
                running = False
            elif event.key == pygame.K_ESCAPE:  
                main_menu()

    if game_over_menu is None: 
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
        size_text = font.render(points[0].get_size_point(), True, (255, 255, 255))
        speed_text = font.render(points[0].get_speed(), True, (255, 255, 255))
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(total_time - elapsed_time, 0) 
        timer_text = font.render(f"Time: {remaining_time}s", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(speed_text, (10, 50))
        screen.blit(size_text, (10, 90))
        screen.blit(timer_text, (10, 130))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        dt = clock.tick(60) / 1000

        if remaining_time <= 0:  
            game_over_menu = GameOverMenu(screen, points[0].score)

    else:  
        next_action = game_over_menu.draw_menu()
        if next_action == "recommencer":
            start_time = pygame.time.get_ticks()
            points[0].reset()
            game_over_menu = None
        elif next_action == "retour_menu":
            main_menu()
        elif next_action == "quitter":
            running = False

    pygame.display.flip()

pygame.quit()
