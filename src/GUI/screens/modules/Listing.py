from abc import ABC

from GUI.screens.Screen import Screen
from pipeline.EventType import EventType as ET


class Listing(Screen, ABC):
    viewOffset: int
    maxViewOffset: int


    def buildList(self, elements):
        listing = []
        for i in range(5):
            if i >= len(elements) - (self.viewOffset * 3):
                listing.append('\_' * 20)
            else:
                listing.append(str(elements[i + (self.viewOffset * 3)]))
        return '\n'.join(listing)

    def scrollUp(self):
        if self.viewOffset > 0:
            self.viewOffset = self.viewOffset - 1
            return True
        return False


    def scrollDown(self):
        if self.viewOffset < self.maxViewOffset:
            self.viewOffset = self.viewOffset + 1
            return True
        return False

    def scrollToTop(self):
        self.viewOffset = 0

    def scrollToBottom(self):
        self.viewOffset = self.maxViewOffset

    def __init__(self, emoji_buttons: [ET], watched_events: [ET]):
        eb = [ET.SCROLL_UP, ET.SCROLL_DOWN]
        eb.extend(emoji_buttons)
        we = [ET.SCROLL_UP, ET.SCROLL_DOWN]
        we.extend(watched_events)
        super().__init__(eb, we)
        self.viewOffset = 0
        self.maxViewOffset = 0
