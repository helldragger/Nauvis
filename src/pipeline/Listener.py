from abc import ABC, abstractmethod

from pipeline.EventType import EventType


class Listener(ABC):


    def __init__(self, watchedEvents: [EventType]):
        self.watchedEvents = watchedEvents

    @abstractmethod
    def update(self, type: EventType, event: object):
        pass
