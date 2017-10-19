# library for add and remove a subscriber

subscribers = []

def register(subscriber):
    if not subscriber in subscribers:
        subscribers.append(subscriber)

def unregister(subscriber):
    if subscriber in subscribers:
        subscribers.remove(subscriber)

def notify_subscribers(*args, **kwargs):
    for subscriber in subscribers:
        subscriber.update(*args, **kwargs)





