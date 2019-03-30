import abc

from BeautifulSoup import BeautifulStoneSoup


class Parser(object):
    """An abstract product, represent parser to parse web content.
     One of its subclasses will be created in factory methods."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, content):
        pass


class HTTPParser(Parser):
    def __call__(self, content):
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')

        filenames = [link['href'] for link in links]
        return '\n'.join(filenames)


class FTPParser(Parser):
    def __call__(self, content):
        lines = content.split('\n')
        filenames = []
        for line in lines:
            # The FTP format typically has 8 columns, split them
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
