class WeatherReport():

    def __init__(self, date, max_temperature, 
                min_temperature, summary, raining_chance, 
                icon):
        self.date = date
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.summary = summary   
        self.raining_chance = raining_chance
        self.icon = icon  