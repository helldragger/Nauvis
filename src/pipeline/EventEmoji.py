from enum import Enum

emojiEq = {}

class EventEmoji(Enum):
    UNKNOWN_EMOJI = "Unknown emoji"

    #navigation
    SCROLL_UP = "👆️"
    SCROLL_DOWN = "👎️"
    TOP = "⤴️"
    BOTTOM = "⤵️"

    CONFIRM = "✔️"
    MODIFY = "📋"
    CANCEL = "❌"

    FFORWARD = "⏭️"
    FORWARD =  "⏩"
    BACKWARD = "⏪"
    FBACKWARD = "⏮️"

    SWITCH_MODE = "🔘"

    INFO = "❔"

    #Anchors
    ZERO = "0️⃣"
    ONE = "1️⃣"
    TWO = "2️⃣"
    THREE = "3️⃣"
    FOUR = "4️⃣"
    FIVE = "5️⃣"
    SIX = "6️⃣"
    SEVEN = "7️⃣"
    EIGHT = "8️⃣"
    NINE = "9️⃣"

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



    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other


for symbol in EventEmoji:
    emojiEq[symbol.value] = symbol