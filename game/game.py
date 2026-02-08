import pygame
from game.settings import settings


def run():
    clock = pygame.time.Clock()
    running = True

    while running:
        surface = pygame.display.get_surface()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(60)

    return

def close():
    pygame.quit()
    quit()