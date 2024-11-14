import pygame
import random
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        for i in range(1, 33):
            pygame.draw.line(screen, "dark green", (32 * i, 0), (32 * i, 512))
            pygame.draw.line(screen, "dark green", (0, 32 * i), (640, 32 * i))
        moleX = 0
        moleY = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xmouse,ymouse = event.pos
                    if moleX*32 <= xmouse <= moleX*32+20 and moleY*32 <= ymouse<= moleY*32+20:
                        screen.fill("light green")
                        for i in range(1, 33):
                            pygame.draw.line(screen, "dark green", (32 * i, 0), (32 * i, 512))
                            pygame.draw.line(screen, "dark green", (0, 32 * i), (640, 32 * i))
                        moleX = random.randrange(1, 20)
                        moleY = random.randrange(1, 16)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(32 * moleX, 32 * moleY)))
                pygame.display.flip()
                clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()