from enum import Enum

from pipeline.EventEmoji import EventEmoji




class EventType(Enum):
    UNIMPLEMENTED = "Unimplemented event type"
    UNKNOWN_EMOJI = "Unknown emoji"

    #events
    ON_REACTION_ADD = "on_reaction_add"
    ON_REACTION_REMOVE = "on_reaction_remove"
    ON_MESSAGE = "on_message"
    ON_MESSAGE_EDIT = "on_message_edit"
    ON_MESSAGE_DELETE = "on_message_delete"

    # navigation
    SCROLL_UP = "🔼"
    SCROLL_DOWN = "🔽"
    TOP = "⤴"
    BOTTOM = "⤵"


    CONFIRM = "✔"
    MODIFY = "📝"
    CANCEL = "✖"

    FFORWARD = "⏭"
    FORWARD = "⏩"
    BACKWARD = "⏪"
    FBACKWARD = "⏮"

    CALENDAR = "🗓"
    LIST = "📜"

    SWITCH_MODE = "🔘"

    CHECKBOX_TICKED = "☑"

    INFO = "ℹ"
    NEW = "🆕"

    # Anchors
    ZERO = "0⃣"
    ONE = "1⃣"
    TWO = "2⃣"
    THREE = "3⃣"
    FOUR = "4⃣"
    FIVE = "5⃣"
    SIX = "6⃣"
    SEVEN = "7⃣"
    EIGHT = "8⃣"
    NINE = "9⃣"

    A = "🇦"
    B = "🇧"
    C = "🇨"
    D = "🇩"
    E = "🇪"
    F = "🇫"
    G = "🇬"
    H = "🇭"
    I = "🇮"
    J = "🇯"
    K = "🇰"
    L = "🇱"
    M = "🇲"
    N = "🇳"
    O = "🇴"
    P = "🇵"
    Q = "🇶"
    R = "🇷"
    S = "🇸"
    T = "🇹"
    U = "🇺"
    V = "🇻"
    W = "🇼"
    X = "🇽"
    Y = "🇾"
    Z = "🇿"


emojiEq = {}

for symbol in EventType:
    special_events = {
        EventType.ON_REACTION_ADD,
        EventType.ON_REACTION_REMOVE,
        EventType.EDIT,
        EventType.DELETE,
        EventType.UNIMPLEMENTED,
        EventType.UNKNOWN_EMOJI
    }
    if symbol not in special_events:
        emojiEq[symbol.value] = symbol

def getEmojiEvent(emoji: str):
    if emoji not in emojiEq.keys():
        return EventType.UNKNOWN_EMOJI
    else:
        return emojiEq.get(emoji)
