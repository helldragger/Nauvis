import asyncio
from sqlite3 import Connection

import discord
from discord import Reaction, User, Message
from discord.ext import commands
import sqlite3 as sql

from discord.ext.commands import Bot

from GUI.screens.Emojicatron import Emojicatron
from GUI.screens.EventList import EventList
from GUI.screens.MainMenu import MainMenu
from GUI.screens.PlanningEdit import PlanningEdit
from GUI.screens.PlanningList import PlanningList
from pipeline.EventType import EventType, getEmojiEvent
from src.db import db

import pipeline.Processing as Pr
from config import *




db:Connection
bot:Bot
db = sql.connect('schedule.db')

db.execute("CREATE TABLE IF NOT EXISTS event ("
       "event_id INTEGER PRIMARY KEY, "
       "name TEXT NOT NULL, "
       "short_desc TEXT NOT NULL, "
       "long_desc TEXT NOT NULL, "
       "version TEXT NOT NULL, "
       "modpack_link TEXT DEFAULT 'Vanilla', "
       "organizer TEXT NOT NULL)")

db.execute("CREATE TABLE IF NOT EXISTS schedule ("
       "id INTEGER PRIMARY KEY, "
       "event_id INTEGER NOT NULL, "
       "all_day BOOLEAN NOT NULL, "
       "date TEXT NOT NULL, "
       "estimated_length TEXT NOT NULL, "
       "reminders TEXT NOT NULL, "
       "moderator TEXT NOT NULL, "
       "state INTEGER NOT NULL ,"
       "FOREIGN KEY (event_id) REFERENCES event(event_id))")


bot = commands.Bot(command_prefix=PREFIX, description='Un bot alien qui fait '
                                                  'le '
                                                  'café.')
### TODO: add prediction de commande sur commandes inconnues


@bot.command()
async def emojicatron(ctx):
    screen = Emojicatron()
    await screen.send(ctx)

@bot.event
async def on_reaction_remove(reac:Reaction, user:User):
    if user.id == bot.user.id:
        return
    await Pr.fireMessageEvent(EventType.ON_REACTION_REMOVE,
                              reac.message.id,
                              (reac, user))
    await Pr.fireMessageEvent(getEmojiEvent(reac.emoji),
                        reac.message.id,
                        (reac, user))


@bot.event
async def on_reaction_add(reac:Reaction, user:User):
    if user.id == bot.user.id:
        return
    await Pr.fireMessageEvent(EventType.ON_REACTION_ADD,
                              reac.message.id,
                              (reac, user))
    await Pr.fireMessageEvent(getEmojiEvent(reac.emoji),
                        reac.message.id,
                        (reac, user))

@bot.event
async def on_message(mess:Message):
    if mess.author.id == bot.user.id:
        return
    await Pr.fireMessageEvent(EventType.ON_MESSAGE,
                        mess.id,
                        (mess))


def is_closed(*_):
    db.commit()
    db.close()

@bot.event
async def on_ready():
    print(bot.user.name, 'aka', bot.user.id, 'est paré au décollage')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #print(db.execute('SELECT * FROM event').fetchall())
    #print(db.execute('SELECT * FROM schedule').fetchall())



bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="NauviBot help panel",
                          description="A Very Nice bot. List of commands are:",
                          color=0xeee657)

    embed.add_field(name=PREFIX+"nauvis",
                    value="Opens the main navigation panel",
                    inline=False)
    embed.add_field(name=PREFIX+"events",
                    value="Let you learn more about our events and tournaments",
                    inline=False)
    embed.add_field(name=PREFIX+"planning",
                    value="Let you view, manage and learn more about the next"
                          "upcoming events",
                    inline=False)
    embed.add_field(name=PREFIX+"cat",
                    value="cat",
                    inline=False)
    embed.add_field(name=PREFIX+"info", value="Gives a little info about the bot",
                    inline=False)
    embed.add_field(name=PREFIX+"help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def nauvis(ctx):
    screen = MainMenu(bot=bot,ctx=ctx)
    await screen.send(ctx)

@bot.command()
async def events(ctx, action=None, *options):
    if action is None:
        await MainMenu(panelIndex=1,bot=bot,ctx=ctx).send(ctx)
    elif action == 'list':
        await EventList().send(ctx)
    else:
        pass

@bot.command()
async def planning(ctx, action=None, *options):
    if action is None:
        await MainMenu(panelIndex=2,bot=bot, ctx=ctx).send(ctx)
    elif action == "list":
        await PlanningList().send(ctx)
    elif action == 'edit':
        await PlanningEdit().send(ctx)
    else:
        pass

@bot.command()
async def info(ctx):
    await MainMenu(panelIndex=9,bot=bot,ctx=ctx).send(ctx)


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

bot.run(TOKEN)
