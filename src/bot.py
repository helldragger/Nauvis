import asyncio
from sqlite3 import Connection

import discord
from discord import Reaction, User
from discord.ext import commands
import sqlite3 as sql

from GUI.screens.Emojicatron import Emojicatron
from GUI.screens.PlanningList import PlanningList
from pipeline.EventType import EventType, getEmojiEvent
from src.db import db
import src.GUI.dialogs as GUI
from GUI.Emojis import Emojis as emo

import pipeline.Processing as Pr
from config import *

db:Connection
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
           "date TEXT NOT NULL, "
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
    await Pr.fireMessageEvent(EventType.REMOVE_REACTION,
                        reac.message.id,
                        (reac, user))
    await Pr.fireMessageEvent(getEmojiEvent(reac.emoji),
                        reac.message.id,
                        (reac, user))


@bot.event
async def on_reaction_add(reac:Reaction, user:User):
    if user.id == bot.user.id:
        return
    await Pr.fireMessageEvent(EventType.ADD_REACTION,
                        reac.message.id,
                        (reac, user))
    await Pr.fireMessageEvent(getEmojiEvent(reac.emoji),
                        reac.message.id,
                        (reac, user))


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


@bot.command()
async def test(ctx):
    name = "Ouroboros"
    short_desc = "Lancer une fusée par minute, a partir d un bus mixte " \
                 "circulaire bordélique à souhait! Venez c'est rigolo :D"
    long_desc = \
    """# OBJECTIF

Envoyer une fusée toutes les 10 minutes afin de produire un total de 100 potions par minute à partir d’une mégabase à bus mixte en circuit fermé !

# JE PEUX VENIR?

Oui, tous les curieux et volontaires sont bienvenus ! Il y a du boulot et du fun pour tout le monde !

# QU’Y A-T-IL DE PRÉVU ?

Des routes, des courses de voitures, de la décoration, du cassage d’autochtones, de la déforestation, du challenge et du partage d’expérience !
Que vous soyez débutant, intermédiaire ou expert, il y a de quoi s’amuser pour vous ! 

– Les moins avancés vont pouvoir désigner les premières usines qui leur seront dédiées, poser leurs questions et évoluer ! Vous pourrez aussi décorer la base et vous amuser sur les terrains de courses !
– Les intermédiaires se chargeront de mener à bien la réalisation et évolution de la base de départ et de préparer les zones de champ libre et de transports !
– Les plus avancés pourront se concentrer sur la logique et le challenge du bus mixte en circuit fermé ainsi que préparer les systèmes de production à grande échelle !

# JE NE PEUX PAS JUSTE REGARDER ?

Et bien si ! Chaque session sera diffusée par un streamer annoncé en avance sur le channel général ! Restez à l’écoute !

# J’AI UNE QUESTION

Et bien, n’aie pas peur de la poser sur le channel #général du projet ! Nous y répondrons avec plaisir !

# COMMENT DÉTERMINE-T-ON QUI FAIT QUOI ?

Afin de pouvoir avoir les permissions d’accéder au projet, vous devez juste nous soumettre votre niveau dans Factorio pour que l’on puisse vous assigner aux tâches les plus adaptées, afin que l’on puisse s’organiser tous ensemble au mieux !

# Y AURA DES MODS ?

Oui ! Ce projet est moddé pour rendre l’objectif final plus faisable et plus fun ! 
La version de Factorio utilisée est la version 16.51 stable et voici la liste des mods du projet :

1. Asphalt roads
2. Color Coding
3. Dectorio
4. FARL
5. Helmod
6. Ore compress
7. Pavement Drive Assist
8. Plate compress
9. Text Plates
10. Upgrade builder and planner"""
    version = "0.16"
    modpack = "https://mega.nz/#F!MfgDXYzb!EaE0RkwIIdmsSgcDLuhTJw"
    organizer = "Helldragger#7021"
    #TODO
    db.execute("INSERT INTO event() VALUES(?,?,?,?,?,?);",
               (name, short_desc, long_desc, version, modpack, organizer))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Nauvibot",
                          description="The best bot ever created on Nauvis! "
                                      ":D WIP",
                          color=EMBEDCOLOR)

    # give info about you here
    embed.add_field(name="Author", value="Helldragger#7021")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite",
                    value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=477269511775453206&permissions=92224&scope=bot)")

    await ctx.send(embed=embed)

bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot",
                          description="A Very Nice bot. List of commands are:",
                          color=0xeee657)

    embed.add_field(name=PREFIX+"add X Y",
                    value="Gives the addition of **X** and **Y**",
                    inline=False)
    embed.add_field(name=PREFIX+"multiply X Y",
                    value="Gives the multiplication of **X** and **Y**",
                    inline=False)
    embed.add_field(name=PREFIX+"greet", value="Gives a nice greet message",
                    inline=False)
    embed.add_field(name=PREFIX+"cat",
                    value="Gives a cute cat gif to lighten up the mood.",
                    inline=False)
    embed.add_field(name=PREFIX+"info", value="Gives a little info about the bot",
                    inline=False)
    embed.add_field(name=PREFIX+"help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


async def message_emojificator(msg, emojis):
    for i in range(len(emojis)):
        await msg.add_reaction(emojis[i][0])



async def message_respondificator(msg, e_list, author):
    def c(r, u):
        print(r.emoji,str([ e[0] for e in e_list]),author,u,r.message.id,msg.id)
        return u == author and str(r.emoji) in [ e[0] for e in e_list] and \
               r.message.id == msg.id
    try:
        print("waiting reaction")
        r, u = await bot.wait_for('reaction_add', timeout=120.0, check=c)
    except asyncio.TimeoutError:
        print("No reaction")
        return ""
    else:
        print("Reaction got")
        return str(r.emoji)
    finally:
        await msg.delete()


async def menu_chooser(ctx, message, emoji_list):
    # Send the menu screen
    menu = await ctx.send(embed=message)
    # Add the dialog controls
    await message_emojificator(menu, emoji_list)
    # return first valid reaction from the author on this message.
    return await message_respondificator(menu, emoji_list, ctx.author)


@bot.command()
async def nauvis(ctx, type=None, act=None, *options):

    if type!=None:
        main_r = emo.INFO.get_emoji()
    else:
        main_r = await menu_chooser(ctx,
                                    GUI.mainmenu_m,
                                    GUI.mainmenu_e)
    print(main_r,type)
    # EVENTS
    if main_r == emo.EVENTS.get_emoji() or type=="events":
        if act != None:
            event_r = emo.INFO.get_emoji()
        else:
            event_r = await menu_chooser(ctx,
                                         GUI.event_m,
                                         GUI.event_e)
        print(event_r, act)
        #LIST📇
        if event_r == emo.LISTING.get_emoji() or act=="list":
            pass
        #ADD
        elif event_r == emo.CREATE.get_emoji() or act=="new":
            pass
        #EDIT
        elif event_r == emo.UPDATE.get_emoji() or act=="edit":
            pass
        #INFO
        else:
            pass
    # PLANNING
    elif main_r == emo.PLANNING.get_emoji() or type=="planning":
        if act != None:
            event_r = emo.INFO.get_emoji()
        else:
            event_r = await menu_chooser(ctx,
                                     GUI.planning_m,
                                     GUI.planning_e)
        #LIST📇
        if event_r == emo.LISTING.get_emoji() or act=="list":
            screen = PlanningList(db)
            await screen.send(ctx)
            pass
        #ADD
        elif event_r == emo.SCHEDULE.get_emoji() or act=="new":
            pass
        #EDIT
        elif event_r == emo.UPDATE.get_emoji() or act=="edit":
            pass
        #INFO
        else:
            pass
    else:
        pass
    # INFOS


    return



@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")



@bot.command()
async def schedule(ctx, mode, type, *args):
    result:str
    if mode == "add" and type == "event":
        result = db.add_event(args)
    if mode == "add" and type == "date":
        result = db.add_date(args)
    if mode == "update" and type == "event":
        result = db.update_event(args)
    if mode == "update" and type == "date":
        result = db.update_date(args)
    if mode == "info" and type == "event":
        result = db.info_event(args)
    if mode == "info" and type == "date":
        result = db.info_date(args)
    await ctx.send(result)


bot.run('NDc3MjY5NTExNzc1NDUzMjA2.Dk5vXQ.Nob0-bavZ9JJJcGxSMnJu0DtjAg')