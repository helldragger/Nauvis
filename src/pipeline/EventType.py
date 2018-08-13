from enum import Enum

from pipeline.EventEmoji import EventEmoji




class EventType(Enum):
    UNIMPLEMENTED = "Unimplemented event type"
    UNKNOWN_EMOJI = "Unknown emoji"

    #events
    ADD_REACTION = "reaction_add"
    REMOVE_REACTION = "reaction_remove"
    EDIT = "message_edit"
    DELETE = "message_delete"

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

    SWITCH_MODE = "🔘"

    INFO = "❔"

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
        EventType.ADD_REACTION,
        EventType.REMOVE_REACTION,
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
