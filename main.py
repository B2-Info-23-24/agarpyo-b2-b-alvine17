import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mouse_pressed = False  

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

    if mouse_pressed:
        player_pos = pygame.mouse.get_pos()
    
    screen.fill("black")

    pygame.draw.circle(screen, "yellow", player_pos, 40)

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

pygame.quit()
