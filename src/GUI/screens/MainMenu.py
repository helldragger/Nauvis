import discord

from GUI.screens.EventList import EventList
from GUI.screens.PlanningEdit import PlanningEdit
from GUI.screens.PlanningList import PlanningList
from GUI.screens.Screen import Screen
from config import EMBEDCOLOR
from pipeline.EventType import EventType


class MainMenu(Screen):
    def __init__(self, panelIndex=0, bot=None, ctx=None):
        # TODO etoffer les embed
        self.ctx = ctx
        self.panels = {
            0: {
                'content': ["?nauvis",
                            EventType.CHECKBOX_TICKED.value + EventType.ONE.value + EventType.TWO.value + EventType.INFO.value],
                'embed':   discord.Embed(title="🌊🌊Welcome to Nauvis "
                                               "Navigation panel! 🌊⛵🌊",
                                         color=EMBEDCOLOR),
                'buttons': []
            },

            1: {
                'content': ["?events",
                            EventType.ZERO.value + EventType.CHECKBOX_TICKED.value + EventType.TWO.value + EventType.INFO.value],
                'embed':   discord.Embed(title="⛵📜Events nav-panel🌊🌊⛵",
                                         color=EMBEDCOLOR),
                'buttons': [EventType.LIST]
            },

            2: {
                'content': ["?planning",
                            EventType.ZERO.value + EventType.ONE.value + EventType.CHECKBOX_TICKED.value + EventType.INFO.value],
                'embed':   discord.Embed(title="🌊🗓Planning nav-panel🌊🌊🌊",
                                         color=EMBEDCOLOR),
                'buttons': [EventType.CALENDAR, EventType.MODIFY]
            },

            9: {
                'content': ["?info",
                            EventType.ZERO.value + EventType.ONE.value + EventType.TWO.value + EventType.CHECKBOX_TICKED.value],
                'embed':   discord.Embed(title="Nauvibot",
                                         description="The best bot ever "
                                                     "created!"
                                                     ":D WIP though",
                                         color=EMBEDCOLOR).add_field(
                    name="Author", value="Helldragger#7021").add_field(
                    name="Server count", value=f"{len(bot.guilds)}").add_field(
                    name="Invite", value="[Invite link]("
                                         "https://discordapp.com/api/oauth2/authorize?client_id=477269511775453206&permissions=92224&scope=bot)"),
                'buttons': []
            }
        }

        emoji_buttons = [
            EventType.ZERO,
            EventType.ONE,
            EventType.TWO, EventType.INFO,
            EventType.CANCEL
        ]

        self.panelIndex = panelIndex
        self.contextual_buttons = self.panels[panelIndex]
        super().__init__(emoji_buttons, emoji_buttons)


    def build(self):
        self.content = self.panels[self.panelIndex]['content']
        self.embed = self.panels[self.panelIndex]['embed']
        self.contextual_buttons = self.panels[self.panelIndex]['buttons']
        pass

    async def update(self, type: EventType, event: object):
        if type == EventType.ZERO and self.panelIndex != 0:
            self.panelIndex = 0
            await self.updateScreen()

        elif type == EventType.ONE and self.panelIndex != 1:
            self.panelIndex = 1
            await self.updateScreen()
        elif type == EventType.LIST and self.panelIndex == 1:
            await EventList().send(self.ctx)
            await self.delete()

        elif type == EventType.TWO and self.panelIndex != 2:
            self.panelIndex = 2
            await self.updateScreen()

        elif type == EventType.CALENDAR and self.panelIndex == 2:
            await PlanningList().send(self.ctx)
            await self.delete()

        elif type == EventType.MODIFY and self.panelIndex == 2:
            await PlanningEdit().send(self.ctx)
            await self.delete()

        elif type == EventType.INFO and self.panelIndex != 9:
            self.panelIndex = 9
            await self.updateScreen()

        elif type == EventType.CANCEL:
            await self.delete()

        pass