from GUI.screens.Screen import Screen
from pipeline.EventType import EventType


class PlanningEdit(Screen):
    # TODO creer l interface
    def __init__(self):
        emoji_buttons = []
        watched_events = []
        super().__init__(emoji_buttons, watched_events)

    def build(self):
        pass

    def update(self, type: EventType, event: object):
        pass
