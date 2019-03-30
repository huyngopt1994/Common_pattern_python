import urllib2

from connector import Connector

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'
    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1-ftp):'.format(domain))

    connection = Connector(protocol)
    try:
        content = connection.read(domain, path)
    except urllib2.URLError as e:
        print('Can not access resource with this method')
    else:
        print(connection.parse(content))
