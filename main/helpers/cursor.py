import pygame

class cursor:
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()

    def get_position(self):
        return self.x, self.y