# Temperatur Api
import os.path

class Sensor:
    def __init__(self, path):
        if os.path.exists(path):
            self.sensor_dir_path = path
        else:
            raise IOError("The Device is not accessible", path)

    @property
    def raw(self):
        tmp_file_name = 'temperature'
        tmp_file_path = os.path.join(self.sensor_dir_path, tmp_file_name)

        with open(tmp_file_path, 'r') as f:
            return int(f.readline())

    @property
    def celsius(self):
        return self.raw / 100

    @property
    def kelvin(self):
        return self.celsius - 273.15

    def __str__(self):
        return f'Sensor "{self.sensor_dir_path}": {self.celsius}c'
