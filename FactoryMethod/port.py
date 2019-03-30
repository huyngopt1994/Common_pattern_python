import abc


class Port(object):
    __metaclass__ = abc.ABCMeta
    """Abstract product. One of it's subclasses will be created in factory methods."""

    @abc.abstractmethod
    def __str__(self):
        pass


class HTTPPort(Port):
    def __str__(self):
        return str(80)


class HTTPSecurePort(Port):
    def __str__(self):
        return str(443)


class FTPPort(Port):
    def __str__(self):
        return str(21)
