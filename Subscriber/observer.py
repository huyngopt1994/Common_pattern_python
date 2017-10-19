from abc import ABCMeta, abstractmethod
# Using abstract Base class to force the inherit class have to implement this interface(abc module)
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass