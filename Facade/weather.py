class Weather:
    """Object to represent an weather within one day which receives an iterable data,
     calculate median temp and store it."""

    def __init__(self, data):
        result = 0
        for r in data:
            result += r
        self.temperature = result / len(data)
