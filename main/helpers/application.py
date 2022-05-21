import pygame

# Event manager
from helpers.event_manager import event

class app:
    
    def __init__(self):

        print("Application Running... ")
        # Initialise
        pygame.init()
        # Set size of window
        width, height = 1200, 1200
        # Name of window
        self.window_title = "2D Map Designer"
        # Create window
        self.window = pygame.display.set_mode((width, height))
        # Define window title
        pygame.display.set_caption(self.window_title)
        # Set window colour
        self.window.fill((0,0,0))
        # Update display
        pygame.display.update()
        # Initialise event manager
        self.event_m = event()
        # Start Main loop
        self.mainloop()

    def mainloop(self):
        running = True

        while running:
            
            # Get time from pygame application
            clock = pygame.time.Clock()

            # Call event manager
            running = self.event_m.update(self.window, clock)
            
            #Update display
            pygame.display.update()

            # Reset Clock
            clock.tick()
                    


    def cleanup(self):
        print("Cleaning up... ")
        return 0

    def destroy(self):
        print("Destroying... ")
        pygame.quit()
        return 0 
