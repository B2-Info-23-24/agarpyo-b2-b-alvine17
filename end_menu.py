import pygame

class GameOverMenu:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font(None, 36)

    def draw_menu(self):
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 400 <= event.pos[0] <= 600:
                        if 200 <= event.pos[1] <= 250:
                            return "recommencer"
                        elif 300 <= event.pos[1] <= 350:
                            return "retour_menu"
                        elif 400 <= event.pos[1] <= 450:
                            pygame.quit()
                            quit()

            self.screen.fill((0, 0, 0))
            self.draw_text("Game Over", (255, 255, 255), 300, 100)
            self.draw_text(f"Score: {self.score}", (255, 255, 255), 300, 150)
            pygame.draw.rect(self.screen, (200, 200, 200), (400, 200, 200, 50))
            self.draw_text("Recommencer", (0, 0, 0), 420, 210)
            pygame.draw.rect(self.screen, (200, 200, 200), (400, 300, 200, 50))
            self.draw_text("Retour au menu", (0, 0, 0), 410, 310)
            pygame.draw.rect(self.screen, (200, 200, 200), (400, 400, 200, 50))
            self.draw_text("Quitter", (0, 0, 0), 450, 410)

            pygame.display.update()

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)
