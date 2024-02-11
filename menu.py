import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

WIDTH, HEIGHT = 1280, 720
menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    menu_running = True
    while menu_running:
        menu_screen.fill(BLACK)
        draw_text("Menu Principal", font, GRAY, menu_screen, 300, 100)
        pygame.draw.rect(menu_screen, GRAY, (150, 200, 200, 50))
        draw_text("Facile", font, BLACK, menu_screen, 200, 210)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= event.pos[0] <= 350:
                    if 200 <= event.pos[1] <= 250:
                        menu_selection("Facile")
        pygame.display.update()


def menu_selection(difficulty):
    mode_running = True
    while mode_running:
        menu_screen.fill(BLACK)
        draw_text("Sélection du mode", font, GRAY, menu_screen, 250, 100)
        pygame.draw.rect(menu_screen, GRAY, (150, 200, 200, 50))
        draw_text("Souris", font, BLACK, menu_screen, 180, 210)
        pygame.draw.rect(menu_screen, GRAY, (150, 300, 200, 50))
        draw_text("Clavier", font, BLACK, menu_screen, 180, 310)
        pygame.draw.rect(menu_screen, GRAY, (150, 400, 200, 50))
        draw_text("Retour", font, BLACK, menu_screen, 180, 410)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= event.pos[0] <= 350:
                    if 200 <= event.pos[1] <= 250:
                        start_game(difficulty, "Souris")  
                    elif 300 <= event.pos[1] <= 350:
                        start_game(difficulty, "Clavier")  
                    elif 400 <= event.pos[1] <= 450:
                        main_menu()  

        pygame.display.update()

def start_game(difficulty, control_mode):
    import main 
    main.start_game(difficulty, control_mode)  

main_menu()
