import urllib
import urllib2


class WeatherProvider:
    def __init__(self):
        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}'

    def get_weather_data(self, city, country):
        encoded_city = urllib.quote(city)
        url = self.api_url.format(encoded_city, country)
        return urllib2.urlopen(url).read()
