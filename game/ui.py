import pygame
import pygame_menu
from game.settings import settings
from game import game

def create_menus():
    main_menu = pygame_menu.Menu(
        'Main Menu',
        settings.width,
        settings.height,
        theme=pygame_menu.themes.THEME_BLUE
    )

    settings_menu = pygame_menu.Menu(
        'Options',
        settings.width,
        settings.height,
        theme=pygame_menu.themes.THEME_BLUE
    )

    def set_resolution(selected, value):
        settings.width, settings.height = value
        settings.apply_display()
        settings.save()

        main_menu.resize(settings.width, settings.height)
        settings_menu.resize(settings.width, settings.height)

    def toggle_fullscreen(value):
        settings.fullscreen = value
        settings.apply_display()
        settings.save()

        main_menu.resize(settings.width, settings.height)
        settings_menu.resize(settings.width, settings.height)

    RESOLUTIONS = [
    ('800 x 600', (800, 600)),
    ('1024 x 768', (1024, 768)),
    ('1280 x 720', (1280, 720)),
    ('1680 x 1050', (1680, 1080)),
    ('1920 x 1080', (1920, 1080)),
    ]
    current_index = 0
    for i, (_, res) in enumerate(RESOLUTIONS):
        if res == (settings.width, settings.height):
            current_index = i
            break
    settings_menu.add.selector(
        'Resolution: ',
        RESOLUTIONS,
        default=current_index,
        onchange=set_resolution
    )            


    settings_menu.add.toggle_switch(
        'Fullscreen ',
        settings.fullscreen,
        onchange=toggle_fullscreen
    )

    settings_menu.add.button('Back', pygame_menu.events.BACK)

    main_menu.add.button('Play', game.run)
    main_menu.add.button('Options', settings_menu)
    main_menu.add.button('Exit', game.close)

    return main_menu