import discord

from GUI.InteractiveEmbed import InteractiveMessage

#TODO add any other possible interaction
class DialogWrapper():

    def __init__(self, context, client, author):
        self.context = context
        self.client = client
        self.author = author
        self.embed = discord.Embed()
        #send message and keep it saved
        self.message = None
        self.build_embed()


    def build_embed(self):
        '''
        Here we build the custom embed.
        '''
        pass

    async def send(self):
        self.message = await self.context.send(embed=self.embed)

    async def scrollUp(self):
        pass

    async def scrollDown(self):
        pass

    async def previous(self):
        pass

    async def next(self):
        pass

    async def quit(self):
        pass

    async def switch_mode(self):
        pass

    async def edit(self):
        pass

    async def validate(self):
        pass

    async def cancel(self):
        pass

    async def stop(self):
        pass


    async def