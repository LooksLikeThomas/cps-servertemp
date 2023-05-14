# Sensor API
import os.path

class BME280:
    def __init__(self, dir_path, fmt=''):
        # exit if sensor is not acessible
        if not os.path.exists(dir_path):
            raise IOError('The Device is not accessible', dir_path)
        
        #set empty formatstring to default
        if fmt == '':
            fmt = 'T:{tmp_c:.2f}C,{tmp_f:.2f}F U:{hum_p:d}% r.F p:{prs_p:d}hPa'
        
        self._fmt = fmt

        # filenames for bme280
        tmp_filename = 'in_temp_input'
        prs_filename = 'in_pressure_input'
        hum_filename = 'in_humidityrealtive_input'
        
        # sensors directory path
        self.sensor_dir_path = dir_path

        # filepaths for all reading files
        self.tmp_file_path = os.path.join(self.sensor_dir_path, tmp_filename)
        self.prs_file_path = os.path.join(self.sensor_dir_path, prs_filename)
        self.hum_file_path = os.path.join(self.sensor_dir_path, hum_filename)
            
    

    # Sensors current realtive humidity in percent
    @property
    def hum_p(self):
        with open(self.hum_file_path, 'r') as f:
            return int(f.readline())
    
    # Sensors current airpressure in hPA
    @property
    def prs_p(self):
        with open(self.prs_file_path, 'r') as f:
            return int(f.readline())

    # Sensors current raw temperature 
    @property
    def tmp_r(self):
        with open(self.tmp_file_path, 'r') as f:
            return int(f.readline())

    # Sensors current temperature in degree celsius
    @property
    def tmp_c(self):
        return self.tmp_r / 100

    # Sensors current temperature in farenheit
    @property
    def tmp_f(self):
        return self.tmp_c * 1.8 + 32

    def get_str_reading(self, fmt=""):
        if fmt == "":
            fmt = self._fmt

        attributes = dir(self)
        d = {attr: getattr(self, attr) for attr in attributes}
        return fmt.format(**d)

    def get_dict_reading(self):
        return dict(
            tmp_c=self.tmp_c,
            tmp_f=self.tmp_f,
            hum_p=self.hum_p,
            prs_p=self.prs_p)

    def __str__(self):
        return f'BME280 "{self.sensor_dir_path}": {self.tmp_c}C'
