import discord
import asyncio

from discord import Embed
from discord import Message


#TODO faire un message qui puisse être sousclassé pour la construction et qui
#TODO réagis à toute interaction avec ses boutons :D

#TODO constructin
#TODO surveillance des reactions
#TODO reaction
class InteractiveMessage(Message):


    def __init__(self, client, buttons, author, timeout=None, **kwargs):
        super().__init__(**kwargs)
        self.client = client
        self.emojis = buttons
        self.author = author
        self.timeout = timeout
        self.build()


    def build(self):
        pass


    def react(self):
        pass

        
    async def wait_for_interaction(self):
        def c(r, u):
            return u == self.author and str(r.emoji) in [e[0] for e in
                                                    self.emojis] and \
                   r.message.id == self.id

        try:
            r, u = await self.client.wait_for('on_reaction',
                                              timeout=self.timeout,
                                           check=c)
        except asyncio.TimeoutError:
            return ""
        else:
            return str(r.emoji)
        finally:
            await self.delete()
