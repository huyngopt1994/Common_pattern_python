import abc

from parser import HTTPParser, FTPParser
from port import HTTPSecurePort, FTPPort, HTTPPort


class AbstractFactory(object):
    """Abstract factory interface provides 3 methods to implement in its subclasses: create_protocol, create_port
    and create_parser.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, is_secure):
        """If is_secure is True, factory tries to make connection secure, otherwise not."""
        self.is_secure = is_secure

    @abc.abstractmethod
    def create_protocol(self):
        pass

    @abc.abstractmethod
    def create_port(self):
        pass

    @abc.abstractmethod
    def create_parser(self):
        pass


class HTTPFactory(AbstractFactory):
    """Concrete factory for building HTTP Connection."""

    def create_protocol(self):
        if self.is_secure:
            return 'https'
        return 'http'

    def create_port(self):
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def create_parser(self):
        return HTTPParser()


class FTPFactory(AbstractFactory):
    """Concrete factory for building HTTP Connection."""

    def create_protocol(self):
        return 'ftp'

    def create_port(self):
        return FTPPort()

    def create_parser(self):
        return FTPParser()
