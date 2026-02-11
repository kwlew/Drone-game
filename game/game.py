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
        settings.width // 2-100,
        settings.height // 2-100
    )

    move_speed = 450

    while running:
        surface = pygame.display.get_surface()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((255, 255, 255))

        surface.blit(drone_img, player_pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:
            player_pos.y -= (move_speed * dt)* 0.707
            player_pos.x -= (move_speed * dt) * 0.707
        if keys[pygame.K_w] and keys[pygame.K_d]:
            player_pos.y -= (move_speed * dt)* 0.707
            player_pos.x += (move_speed * dt) * 0.707
        if keys[pygame.K_s] and keys[pygame.K_d]:
            player_pos.y += (move_speed * dt)* 0.707
            player_pos.x += (move_speed * dt) * 0.707
        if keys[pygame.K_s] and keys[pygame.K_a]:
            player_pos.y += (move_speed * dt)* 0.707
            player_pos.x -= (move_speed * dt) * 0.707
        if keys[pygame.K_w] and not keys[pygame.K_d] and not keys[pygame.K_a]:
            player_pos.y -= move_speed * dt
        if keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            player_pos.y += move_speed * dt
        if keys[pygame.K_a] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            player_pos.x -= move_speed * dt
        if keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
            player_pos.x += move_speed * dt
        
        print(player_pos.x)
        print(player_pos.y)
                
        if player_pos.x > settings.width:
            player_pos.x = (player_pos.x-settings.width-200)
        if player_pos.x < 0-200:
            player_pos.x = (player_pos.x+settings.width+200)
        if player_pos.y < 0:
            player_pos.y = (player_pos.y+settings.height+200)
        if player_pos.y > settings.height:
            player_pos.y = (player_pos.y-settings.height-200)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    return

def close():
    pygame.quit()
    quit()