from observable import register, notify_subscribers, subscribers
from observer import Observer

class Saigon(Observer):
    def __init__(self):
        register(self)

    def update(self,*args,**kwargs):
        print('Saigon received: {0}\n{1}'.format(args, kwargs))

class DaNang(Observer):
    def __init__(self):
        register(self)

    def update(self,*args, **kwargs):
        print('Danang recived: {0}\n{1}'.format(args, kwargs))


class Hanoi():
    def __init__(self):
        pass

    def update(self, *args, **kwargs):
        print('Danang recived: {0}\n{1}'.format(args, kwargs))


if __name__ == "__main__":
    saigon_observer = Saigon()
    danang_observer = DaNang()
    hanoi_observer = Hanoi()

    notify_subscribers('Khoi', something='Saigon have heavy rain')