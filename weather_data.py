import requests

class WeatherData:
    def __init__(self, latitude, longitude):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.latitude = latitude
        self.longitude = longitude

    def get_weather_data(self):
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hourly": "temperature_2m,weather_code"
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

