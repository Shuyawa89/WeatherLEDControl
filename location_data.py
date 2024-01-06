import geocoder

class LocationData:
    @staticmethod
    def get_lat_lon(location_name):
        result = geocoder.osm(location_name)
        if result.ok:
            return result.latlng
        else:
            raise ValueError("Location not found")
