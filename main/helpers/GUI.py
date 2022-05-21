import pygame
import pygame_gui

class gui

    def __init__(self):

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == test_button:
                    # Update GUI display, or call some function
                    print('Test button pressed')
        return 0 