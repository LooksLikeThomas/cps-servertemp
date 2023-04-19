# CPS Seerverraumsteuerung
from temp import Sensor

def main() :
    bme280 = Sensor('./SensorTest')
    print(bme280)

if __name__ == '__main__' :
    main()