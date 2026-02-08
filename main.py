import pygame
from game import ui
from game.settings import settings

pygame.init()
settings.surface = pygame.display.set_mode((settings.width, settings.height))

icon = pygame.image.load("assets/drone.png").convert_alpha()
pygame.display.set_icon(icon)

settings.load()
settings.apply_display()

main_menu = ui.create_menus()
main_menu.mainloop(pygame.display.get_surface())