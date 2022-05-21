import pygame
import pygame_gui

# Import Main

class gui:

    def __init__(self):
        # Fetch pygame window size
        self.width, self.height = pygame.display.get_surface().get_size()
        # Initialise GUI manager
        self.manager = pygame_gui.UIManager((self.width, self.height))
        # Show FPS config
        self.gui_fps_visible = False
        self.gui_show_fps = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Toggle FPS',
                                             manager=self.manager)

    def update(self, pygame_event, clock, pygame_window):
        #Update time_delta
        time_delta = clock.tick(60)/1000.0

        if pygame_event.type == pygame_gui.UI_BUTTON_PRESSED:
            
            # GUI items to be processed go here...
            if pygame_event.ui_element == self.gui_show_fps:
                  self.gui_fps_visible = not self.gui_fps_visible

        

        self.manager.process_events(pygame_event)
        self.manager.update(time_delta)
        self.manager.draw_ui(pygame_window)

    # Time dependent GUI component
    def fps_counter_toggle(self, pygame_window, clock):
        
            if self.gui_fps_visible:
                print(clock.get_fps())
                font = pygame.font.Font('freesansbold.ttf', 16)
                text = font.render('{}'.format(clock.get_fps()), True, (255, 255, 255), False)
                textRect = text.get_rect()
                pygame_window.blit(text, textRect)
