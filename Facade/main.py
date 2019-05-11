from cache import Cache
from converter import Converter
from parser import Parser
from provider import WeatherProvider
from weather import Weather

caching_file = 'my_file'


class MyFacade:
    def get_forecast(self, city, country):
        cache = Cache(caching_file)
        cache_result = cache.load()
        if cache_result:
            return cache_result

        weather_provider = WeatherProvider()
        weather_data = weather_provider.get_weather_data(city, country)
        parser = Parser()
        parsed_data = parser.parser_weather_data(weather_data)
        weather = Weather(parsed_data)
        converter = Converter()
        temperature_celcius = converter.from_kelvin_to_celcius(weather.
                                                               temperature)
        cache.save(temperature_celcius)
        return temperature_celcius


if __name__ == '__main__':
    my_facade = MyFacade()
    print(my_facade.get_forecast('London', 'UK'))
