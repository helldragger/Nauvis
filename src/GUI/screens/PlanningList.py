import discord

from GUI.screens.Screen import Screen
from pipeline.EventType import EventType as ET
from db.PlannedEvent import PlannedEvent

class PlanningList(Screen):
    dateOffset:int
    viewOffset:int
    maxViewOffset:int
    weekMode:bool
    planning:[PlannedEvent]

    def __init__(self, database):
        self.viewOffset = 0
        self.maxViewOffset = 1
        self.dateOffset = 0
        self.db = database
        self.weekMode = True


        watched_events = [
            ET.SCROLL_UP,
            ET.SCROLL_DOWN,
            ET.BACKWARD,
            ET.FORWARD,
            ET.SWITCH_MODE,
            ET.CANCEL
        ]
        emoji_button = [
            (ET.SCROLL_UP, ""),
            (ET.SCROLL_DOWN, ""),
            (ET.SWITCH_MODE, ""),
            (ET.BACKWARD, ""),
            (ET.FORWARD, ""),
            (ET.CANCEL, "")
        ]
        super().__init__(emoji_button, watched_events)




    async def update(self, type: ET, event: object):
        if type == ET.SCROLL_DOWN:
            if self.viewOffset < self.maxViewOffset:
                self.viewOffset = self.viewOffset + 1
                await self.updateScreen()
        if type == ET.SCROLL_UP:
            if self.viewOffset > 0:
                self.viewOffset = self.viewOffset - 1
                await self.updateScreen()
        if type == ET.BACKWARD:
            if self.dateOffset > -12:
                self.dateOffset = self.dateOffset - 1
                await self.updateScreen()
        if type == ET.FORWARD:
            if self.dateOffset < 12:
                self.dateOffset = self.dateOffset + 1
                await self.updateScreen()
        if type == ET.SWITCH_MODE:
            self.weekMode = not self.weekMode
            self.dateOffset = 0
            self.viewOffset = 0
            await self.updateScreen()
        if type == ET.CANCEL:
            await self.delete()
        pass

    def build(self):
        self.content = []
        #self.planning = yada yada
        self.planning = [
            PlannedEvent("20:30 11/08",
                         "Projet Ouroboros",
                         "1",
                         "10",
                         "#projet-ouroboros"),

            PlannedEvent("19:30 16/08",
                         "Archipelago",
                         "7",
                         "7",
                         "#archipel-factorio"),

            PlannedEvent("20:00 18/08",
                         "Tournoi PVP par équipe",
                         "2",
                         "11",
                         "#team-pvp-event"),

            PlannedEvent("19:30 23/08",
                         "Archipelago",
                         "7",
                         "8",
                         "#archipel-factorio"),

            PlannedEvent("20:30 25/08",
                         "Projet Ouroboros",
                         "1",
                         "12",
                         "#projet-ouroboros"),

            PlannedEvent("23:00 31/08",
                         "Entropy",
                         "666",
                         "1",
                         "#entropy"),
        ]
        self.maxViewOffset = (len(self.planning)-2)//3



        import datetime as dt

        from datetime import date
        def formatDate(d:date):
            return '/'.join([str(d.day), str(d.month), str(d.year)])
        today = dt.date.today()

        if self.weekMode:
            weekBeginning = dt.date(today.year,
                                    today.month,
                                    today.day - today.weekday())
            weekBeginning += dt.timedelta(days=self.dateOffset*7)
            #weekEnding = weekBeginning + dt.timedelta(days=7)
            self.content.append('🗓 *'+formatDate(weekBeginning)+'*')
        else:
            monthBeginning = dt.date(today.year,
                                     today.month,
                                     1)
            mod = 0
            if monthBeginning.month + self.dateOffset > 12:
                mod = 1
            elif monthBeginning.month + self.dateOffset < 1:
                mod = -1
            monthBeginning = dt.date(today.year+mod,
                                     ((today.month -1 + self.dateOffset)%12) +1,
                                     1)

            mod = 0
            if monthBeginning.month + self.dateOffset + 1 > 12:
                mod = 1
            elif monthBeginning.month + self.dateOffset + 1 < 1:
                mod = -1
            #monthEnding = dt.date(today.year+mod,
            #                     ((today.month -1 + self.dateOffset + 1)%12)
                #  +1,
            #                     1)
            self.content.append('🗓 *'+formatDate(monthBeginning) +'*')

        mode = '⚪ **Week** / Month' if self.weekMode else '🔘 Week / **Month**'
        self.content.append(mode)
        from config import EMBEDCOLOR
        self.embed = discord.Embed(color=EMBEDCOLOR)
        #decale de 3 si il y a plus de 5 evenements dans la lsite des
        # evenements, puis par suite de 3.
        upcoming_events = []
        for i in range(5):
            if i >= len(self.planning)-(self.viewOffset*3):
                upcoming_events.append('\_'*20 )
            else:
                upcoming_events.append(str(self.planning[i+(self.viewOffset*3)]))
        self.embed.add_field(name="Upcoming events",
                             value='\n'.join(upcoming_events),
                             inline=False)
        pass

    def rebuild(self):

        pass
