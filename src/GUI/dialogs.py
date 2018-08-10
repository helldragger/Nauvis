import discord

from src.GUI.Emojis import Emojis as e


dialog_color = 0xeee657

def gen_dialog(title:str, options:[e],
               description=""):
    dialog = discord.Embed(title=title,
                           description=description,
                           color=dialog_color)
    for option in options:
        dialog.add_field(name=option[0], value=option[1], inline=True)

    return dialog


mainmenu_e = [e.EVENTS.value, e.PLANNING.value, e.INFO.value]
mainmenu_m = gen_dialog(title="Welcome to Nauvis, fellow factorian!",
                        options= mainmenu_e,
                        description="What can I do for you today?")


event_e = [e.LISTING.value, e.CREATE.value, e.UPDATE.value, e.INFO.value]
event_m = gen_dialog(title="Okay, what do you wanna do concerning those "
                           "events?",
                        options= event_e,
                        description="Wanna see what surprise we have in stock?")


planning_e = [e.LISTING.value, e.SCHEDULE.value, e.UPDATE.value, e.INFO.value]
planning_m = gen_dialog(title="I wonder where I lost the plann.... Oh wait, "
                              "there it is!",
                        options= planning_e,
                        description="What do you wanna see?")
help_dialog = gen_dialog

