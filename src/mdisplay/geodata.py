import os
import json
from pathlib import Path
from geopy import Nominatim


class GeoData:

    def __init__(self):
        self.cache_dir = os.path.join(str(Path.home()), '.cache', 'geodata')
        self.cache_path = os.path.join(self.cache_dir, 'geodata.json')
        self.full_inet = True
        if not os.path.isdir(self.cache_dir):
            try:
                os.mkdir(self.cache_dir)
                self.full_inet = False
            except:
                pass
            self.cache = {}
        else:
            if os.path.exists(self.cache_path):
                with open(self.cache_path, 'r') as f:
                    self.cache = json.load(f)
                    self.full_inet = False
            else:
                self.cache = {}
        if self.full_inet:
            raise UserWarning('GeoData : unable to locate cache, switching to full-Internet mode')
        self.locator = None

    def get_coords(self, name):
        """
        Get coordinates for corresponding geocode
        :param name: The geodcode
        :return: Coordinates (lon, lat) in degrees
        """
        name = name.lower().strip()
        if not self.full_inet and name in self.cache.keys():
            return self.cache[name]
        else:
            self.locator = Nominatim(user_agent='openstreetmaps')
            loc = self.locator.geocode(name)
            point = (loc.longitude, loc.latitude)
            if not self.full_inet:
                self.cache[name] = point
                with open(self.cache_path, 'w') as f:
                    json.dump(self.cache, f)
            return point

if __name__ == '__main__':
    gd = GeoData()
    gd.get_coords('Dakar')
    gd.get_coords('Natal')