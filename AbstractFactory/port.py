import abc


class Port(object):
    __metaclass__ = abc.ABCMeta
    """An abstract product, represents port to connect. One of its subclasses will be created in factory methods.
    """

    @abc.abstractmethod
    def __str__(self):
        pass


class HTTPPort(Port):
    """A concrete product with represents http port."""

    def __str__(self):
        return '80'


class HTTPSecurePort(Port):
    """A concrete product which represents https port."""

    def __str__(self):
        return '443'


class FTPPort(Port):
    """A concrete product which represents https port."""

    def __str__(self):
        return '21'
