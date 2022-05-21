import pygame

# Import Custom API's
from helpers.cursor import cursor
from helpers.GUI import gui

# This class is used to manage all events during runtime
class event:
    def __init__(self):
        # Initialise all class instances
        self.e_cursor = cursor()
        self.e_gui = gui()

    # This method is updated after each pygame runcycle
    def update(self, pygame_window, clock):

        # Updates that are event critical
        for pygame_event in pygame.event.get():

                # Exit Condition
                if pygame_event.type == pygame.QUIT:
                    return False

                # Update State of Class
                self.e_cursor.update()
                self.e_gui.update(pygame_event, clock, pygame_window)

        # Updates that are time critical
        self.e_gui.fps_counter_toggle(pygame_window, clock)
        # Acknowledge that game is still alive
        return True
        