import abc
import logging
import urllib2

from BeautifulSoup import BeautifulStoneSoup

from port import HTTPSecurePort, HTTPPort, FTPPort

logger = logging.getLogger(__name__)


class Connector(object):
    """Abstract class to connect to remote resource."""
    __metaclass__ = abc.ABCMeta  # Declares class as abstract class

    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    @abc.abstractmethod
    def parse(self):
        """Parses web content.
        This method should be redefined in the run time
        """
        pass

    @abc.abstractmethod
    def protocol_factory_method(self):
        """A factory method that must be redenied in subclass."""
        pass

    @abc.abstractmethod
    def port_factory_method(self):
        """Another factory method that must be redefined in the subclass."""
        pass

    def read(self, host, path):
        """A generic method for all subclasses, reads web content."""
        url = '{protocol}://{host}:{port}{path}'.format(protocol=self.protocol, host=host, port=self.port, path=path)
        print('Connecting to', url)
        return urllib2.urlopen(url, timeout=2).read()


class HTTPConnector(Connector):
    """A concrete creator that creates a HTTP connector and sets in runtime all it's attributes."""

    def protocol_factory_method(self):
        """return protocol"""
        if self.is_secure:
            return 'https'
        return 'http'

    def port_factory_method(self):
        """Here HTTPPort and HTTPSecurePort are concrete objects, created by factory method."""
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def parse(self, content):
        """Parses web content."""
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')

        filenames = [link['href'] for link in links]
        return '\n'.join(filenames)


class FTPConnector(Connector):
    """A concrete creator that creates a FTP connector and sets in runtime all it's attributes."""

    def protocol_factory_method(self):
        return 'ftp'

    def port_factory_method(self):
        return FTPPort()

    def parse(self, content):
        lines = content.split('\n')
        filenames = []
        for line in lines:
            # The FTP format typically has 8 columns, split them
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])

        return '\n'.join(filenames)
