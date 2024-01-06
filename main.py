from weather_data import WeatherData
from process_response import ProcessResponse
from location_data import LocationData
from pprint import pprint

def main():
    location_name = "つくば市"
    try:
        lat_lon = LocationData.get_lat_lon(location_name)
        wether_data = WeatherData(lat_lon[0], lat_lon[1])
        wether_responce = wether_data.get_weather_data()

        latestdata, temperature, weather_code = ProcessResponse.extract_wether_data(wether_responce)

        print(f"Location: {location_name}")
        print(f"Latest Weather Data: {latestdata}")
        print(f"Temperature: {temperature}°C, Weather Code: {weather_code}")

        pprint(wether_responce)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()