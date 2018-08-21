from abc import abstractmethod

from discord import Embed, File, Message

import pipeline.Processing as Pr
from pipeline.EventType import EventType, getEmojiEvent
from pipeline.Listener import Listener


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
    contextual_buttons: [EventType]

    @abstractmethod
    def __init__(self,emoji_buttons:[EventType], watched_events: [
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
        self.contextual_buttons = []


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
            for ev in self.emoji_buttons:
                if getEmojiEvent(ev.value) != EventType.UNKNOWN_EMOJI:
                    await self.registerButton(ev)
                else:
                    Pr.registerScreen(self, ev)
            for button in self.contextual_buttons:
                await self.registerButton(button)



    async def registerButton(self, emojiButton):
        await self.msg_ref.add_reaction(emojiButton.value)
        Pr.registerScreenButton(self, emojiButton)

    async def unregisterButton(self, emojiButton):
        await self.msg_ref.remove_reaction(emojiButton.value,
                                           self.msg_ref.author)  # Pr.unregisterScreenButton(self, emojiButton)


    async def updateScreen(self):
        if self.sent and not self.deleted:
            for button in self.contextual_buttons:
                await self.unregisterButton(button)
            self.build()
            await self.msg_ref.edit(content='\n'.join(self.content),
                                    embed=self.embed,
                                    delete_after=self.delete_after)
            for button in self.contextual_buttons:
                await self.registerButton(button)

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
        self.content = ["SAMPLE SCREEN, NOT READY YET"]
        pass
