from enum import Enum


class Emojis(Enum):
    YES = ("🇾", "Yes")
    NO = ("🇳", "No")
    CANCEL = ("🛑", "Cancel this action")

    EVENTS = ("🎪", "Show me the event list!")
    PLANNING = ("📆", "When are the next upcoming events?")

    LISTING = ("📇","Show me what you got!")

    CREATE = ("🆕", "Create a new event")
    SCHEDULE = ("📅","Schedule a new event")

    UPDATE = ("🔥", "Update")
    INFO = ("🤔", "Tell me more..")

    WEEK = ("⏩", "This week!")
    MONTH = ("⏭️", "This month!")

    FBACKWARD = ("⏮️", "+1 month")
    BACKWARD = ("⏪", "")
    VALIDATE = ("✅", "")
    FORWARD = ("⏩", "")
    FFORWARD = ("⏭️", "")

    CANCELED = ("", "This event has been canceled.")
    ENDED = ("","This event has ended.")
    RESCHEDULED = ("","This event has been rescheduled.")
    ON_AIR = ("","This event is currently open!")
    PLANNED = ("","This event is coming soon!")
    WAITING = ("", "This event has yet to be scheduled.")

    def __init__(self, emoji, desc):
        self.emoji = emoji
        self.desc = desc

    def get_emoji(self):
        return self.emoji

    def get_desc(self):
        return self.desc



