from GUI.screens.Screen import Screen
from pipeline.EventType import EventType


class Emojicatron(Screen):

    def __init__(self):
        emoji_buttons = [
            (EventType.C, "End the emojitest")
        ]
        watched_events = [EventType.ON_REACTION_ADD, EventType.C]

        super().__init__(emoji_buttons, watched_events)

    def build(self):
        self.content.append("End this emoji code test with the 🇨 emoji "
                            "reaction")
        pass

    async def update(self, type: EventType, event):
        if type == EventType.ON_REACTION_ADD:
             # event = (Reaction, User)
            print("EMOJI> Received", event[0].emoji, "emoji")
        if type == EventType.C:
            await self.delete()
        pass