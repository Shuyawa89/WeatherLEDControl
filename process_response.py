class ProcessResponse:
    @staticmethod
    def extract_wether_data(data):
        leastdata = data['hourly']['time'][-1]
        temperature = data['hourly']['temperature_2m'][-1]
        weather_code = data['hourly']['weather_code'][-1]
        return leastdata, temperature, weather_code