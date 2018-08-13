from GUI.screens.Screen import Screen
from pipeline.EventType import EventType

class MainMenu(Screen):
    def __init__(self):
        emoji_buttons = [
            EventType.ZERO,
            EventType.ONE,
            EventType.TWO,
            EventType.I,
            EventType.CANCEL
        ]
        

        super().__init__(emoji_buttons, emoji_buttons)

    def build(self):
        pass

    def update(self, type: EventType, event: object):
        pass