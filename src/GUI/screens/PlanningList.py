import sqlite3 as sql

import discord

from GUI.screens.modules.Listing import Listing
from db.PlannedEvent import PlannedEvent
from pipeline.EventType import EventType as ET


class PlanningList(Listing):
    dateOffset:int
    weekMode:bool
    planning:[PlannedEvent]

    def __init__(self):
        self.dateOffset = 0
        self.db = sql.connect('schedule.db')
        self.weekMode = True


        watched_events = [ET.SWITCH_MODE,
            ET.BACKWARD,
            ET.FORWARD,
            ET.CANCEL
        ]
        emoji_button = [
            ET.SWITCH_MODE,
            ET.BACKWARD,
            ET.FORWARD,
            ET.CANCEL
        ]
        super().__init__(emoji_button, watched_events)




    async def update(self, type: ET, event: object):
        if type == ET.SCROLL_DOWN:
            if self.scrollDown():
                await self.updateScreen()
        if type == ET.SCROLL_UP:
            if self.scrollUp():
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
            self.scrollToTop()
            await self.updateScreen()
        if type == ET.CANCEL:
            await self.delete()
        pass

    def build(self):
        import datetime as dt
        self.content = []
        #self.planning = yada yada
        #TODO update with real data
        self.planning = [
            PlannedEvent(False, "20:30 11/08", dt.timedelta(hours=3), [],
                         "Projet Ouroboros",
                         "1",
                         "10",
                         "#projet-ouroboros"),

            PlannedEvent(False, "19:30 16/08", dt.timedelta(hours=3), [],
                         "Archipelago",
                         "7",
                         "7",
                         "#archipel-factorio"),

            PlannedEvent(False, "20:00 18/08", dt.timedelta(hours=3), [],
                         "Tournoi PVP par équipe",
                         "2",
                         "11",
                         "#team-pvp-event"),

            PlannedEvent(False, "19:30 23/08", dt.timedelta(hours=3), [],
                         "Archipelago",
                         "7",
                         "8",
                         "#archipel-factorio"),

            PlannedEvent(False, "20:30 25/08", dt.timedelta(hours=3), [],
                         "Projet Ouroboros",
                         "1",
                         "12",
                         "#projet-ouroboros"),

            PlannedEvent(False, "23:00 31/08", dt.timedelta(hours=3), [],
                         "Entropy",
                         "666",
                         "1",
                         "#entropy"),
        ]
        self.maxViewOffset = (len(self.planning)-2)//3





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

        self.embed.add_field(name="Upcoming events",
                             value=self.buildList(self.planning),
                             inline=False)
        pass

    def rebuild(self):

        pass
