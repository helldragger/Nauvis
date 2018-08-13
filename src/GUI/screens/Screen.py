from abc import abstractmethod

from discord import Embed, File, Message

from pipeline.EventType import EventType
from pipeline.Listener import Listener
import pipeline.Processing as Pr


class Screen(Listener):
    content: [str]
    tts: bool
    embed: Embed
    files: [File]
    delete_after: float
    nonce: int
    sent: bool
    deleted: bool
    edited: bool
    msg_ref: Message

    @abstractmethod
    def __init__(self,emoji_buttons:[(str, str)], watched_events: [
        EventType]):
        super().__init__(watched_events)
        self.sent = False
        self.edited = False
        self.deleted = False
        self.msg_ref = None
        self.content = []
        self.tts = False
        self.embed = None
        self.files = None
        self.delete_after = None
        self.emoji_buttons = emoji_buttons




    async def send(self, context):
        if not self.sent:
            # builds and send the message
            self.build()
            self.msg_ref = await context.send(content='\n'.join(self.content),
                                              tts=self.tts, embed=self.embed,
                                              files=self.files,
                                              delete_after=self.delete_after)
            self.sent = True
            # register the listener
            Pr.registerScreen(self, self.watchedEvents)
            for emoji in self.emoji_buttons:
                e = emoji[0]
                print("adding reaction "+ e.name + " as "+ e.value)
                await self.msg_ref.add_reaction(emoji[0].value)

    async def updateScreen(self):
        if self.sent and not self.deleted:
            self.build()
            await self.msg_ref.edit(content='\n'.join(self.content),
                                    embed=self.embed,
                                    delete_after=self.delete_after)

    async def delete(self):
        if self.sent and not self.deleted:
            # Delete the message
            await self.msg_ref.delete()
            # Unregister events
            Pr.unregisterScreen(self)
            # Mark it as deleted
            self.deleted = True

    @abstractmethod
    def build(self):
        pass
