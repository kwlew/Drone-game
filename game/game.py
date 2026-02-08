import pygame
from game.settings import settings
from game.utils import asset_path

def run():
    clock = pygame.time.Clock()
    running = True

    drone_img = pygame.image.load(
        asset_path("drone.png")
    ).convert_alpha()

    player_pos = pygame.Vector2(
        settings.width // 2 - 100,
        settings.height // 2 - 100
    )

    while running:
        surface = pygame.display.get_surface()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((255, 255, 255))

        surface.blit(drone_img, player_pos)

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

    return

def close():
    pygame.quit()
    quit()