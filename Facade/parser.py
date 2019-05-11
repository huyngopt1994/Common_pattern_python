import datetime
import json


class Parser:
    def parser_weather_data(self, weather_data):
        parsed_data = json.loads(weather_data)
        start_date = None
        result = []

        for data in parsed_data['list']:
            date = datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
            start_date = start_date or date
            if start_date.day != date.day:
                return result
            result.append(data['main']['temp'])
