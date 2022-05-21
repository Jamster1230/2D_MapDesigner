import pygame

# Event manager
from helpers.event_manager import event

class app:
    
    def __init__(self):

        print("Application Running... ")
        # Set size of window
        width, height = 1200, 1200
        # Create window
        self.window = pygame.display.set_mode((width, height))
        # Define window title
        pygame.display.set_caption('2D Map Designer')
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
            for event in pygame.event.get():

                # Exit Condition
                if event.type == pygame.QUIT:
                    running = False
                
                else:
                    self.event_m.update()
                    


    def cleanup(self):
        print("Cleaning up... ")
        return 0

    def destroy(self):
        print("Destroying... ")
        pygame.quit()
        return 0 
