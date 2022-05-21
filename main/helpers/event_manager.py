# Import Custom API's
from helpers.cursor import cursor
from helpers.GUI import gui

# This class will be called upon each pygame cycle
class event:
    def __init__(self):
        # Initialise all class instances
        self.e_cursor = cursor()
        self.e_gui = gui()

    def update(self):
        # Update classes
        self.e_cursor.update()
        self.e_gui.update()