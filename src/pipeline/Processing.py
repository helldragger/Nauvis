# Type => ListenerDict (id => [object])
from pipeline.EventType import EventType
from pipeline.Listener import Listener


msgWatcherRegistry = {}
msgListenerRegistry = {}

globalWatcherRegistry = {}
globalListenerRegistry = {}


async def fireMessageEvent(event_type: EventType, msg_id: int,
                           event_data: object):
    try:
        for listener in msgWatcherRegistry.get(event_type).get(msg_id):
            await listener.update(event_type, event_data)
    except AttributeError:
        pass
    except TypeError:
        pass
    print("INFO>" + event_type.name + " message event triggered on msg#" + str(
        msg_id))
    await fireGlobalEvent(event_type, event_data)


async def fireGlobalEvent(event_type: EventType, event_data: object):
    try:
        for listener in globalWatcherRegistry.get(event_type):
            await listener.update(event_type, event_data)
    except TypeError:
        pass

    print("INFO>" + event_type.name + " global event triggered")


def registerScreen(ref, *types: EventType):
    if not ref.sent or ref.deleted:
        raise RuntimeError("Cannot register this Screen, either not sent or "
                           "already deleted.")
    if ref.msg_ref is None:
        raise RuntimeError("There is no message ref to register.")
    if type(types[0]) == list:
        types = types[0]

    id = ref.msg_ref.id
    for T in types:
        if T not in msgWatcherRegistry.keys():
            msgWatcherRegistry.setdefault(T, {
                id: {ref}
            })
        elif id not in msgWatcherRegistry.get(T):
            msgWatcherRegistry.get(T)[id] = {ref}
        else:
            msgWatcherRegistry.get(T).get(id).add(ref)

        if ref not in msgListenerRegistry.keys():
            msgListenerRegistry.setdefault(ref, {T})
        else:
            msgListenerRegistry.get(ref).add(T)

    print("INFO>" + str(ref.msg_ref.id) + " screen has been registered")


def registerScreenButton(ref, T: EventType):
    if not ref.sent or ref.deleted:
        raise RuntimeError("Cannot register this Screen, either not sent or "
                           "already deleted.")
    if ref.msg_ref is None:
        raise RuntimeError("There is no message ref to register.")

    id = ref.msg_ref.id
    if T not in msgWatcherRegistry.keys():
        msgWatcherRegistry.setdefault(T, {
            id: {ref}
        })
    elif id not in msgWatcherRegistry.get(T):
        msgWatcherRegistry.get(T)[id] = {ref}
    else:
        msgWatcherRegistry.get(T).get(id).add(ref)

    if ref not in msgListenerRegistry.keys():
        msgListenerRegistry.setdefault(ref, {T})
    else:
        msgListenerRegistry.get(ref).add(T)


def unregisterScreen(ref):
    for type in msgListenerRegistry.get(ref):
        del msgWatcherRegistry[type][ref.msg_ref.id]
    del msgListenerRegistry[ref]
    print("INFO>" + str(ref.msg_ref.id) + " screen has been unregistered")


def unregisterScreenButton(ref, T: EventType):
    if msgWatcherRegistry[T][ref.msg_ref.id] is None:
        raise RuntimeError("Event not registered.")
    del msgWatcherRegistry[T][ref.msg_ref.id]
    del msgListenerRegistry[ref][T]
    print("INFO>" + str(ref.msg_ref.id) + " screen button ", T, "has been " \
                                                                "unregistered")


def registerGlobalListener(ref: Listener, *types: EventType):
    if type(types[0]) == list:
        types = types[0]
    for T in types:
        if T not in globalWatcherRegistry.keys():
            globalWatcherRegistry.setdefault(T, {ref})
        elif id not in globalWatcherRegistry.get(T):
            globalWatcherRegistry.get(T)[id] = {ref}
        else:
            globalWatcherRegistry.get(T).add(ref)

        if ref not in globalListenerRegistry.keys():
            globalListenerRegistry.setdefault(ref, {T})
        else:
            globalListenerRegistry.get(ref).add(T)

    print("INFO>" + str(ref) + " has been registered")


def unregisterGlobalListener(ref: Listener):
    for type in globalListenerRegistry.get(ref):
        del globalWatcherRegistry[type][ref]
    del globalListenerRegistry[ref]
    print("INFO>" + str(ref) + " has been unregistered")
