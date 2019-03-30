import urllib2

from factory import HTTPFactory, FTPFactory


class Connector(object):
    """A client."""

    def __init__(self, protocol):
        """Factory is a AbstractFactory instance with creates all attributes of
         a connector according to factory class."""
        if protocol not in [0, 1]:
            print('Sorry, wrong answer')
            return
        factory = None
        if protocol == 0:
            is_secure = bool(input('Use secure connection? (1-yes, 0 -no)'))
            factory = HTTPFactory(is_secure)
        elif protocol == 1:
            is_secure = False
            factory = FTPFactory(is_secure)

        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parser()

    def read(self, host, path):
        url = '{}://{}:{}{}'.format(self.protocol, host, self.port, path)
        print('Connecting to {}'.format(url))
        return urllib2.urlopen(url, timeout=2).read()
