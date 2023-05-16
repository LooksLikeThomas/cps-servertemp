# CPS Serverraumsteuerung

import sys
import sensor
import logging
import time
import csv_log

def main():
    # formatting strings
    date_format = '%Y-%m-%d %H:%M:%S'
    console_format = '%(asctime)s - %(name)s - %(msg)s'
    sensor_str_format = 'Temperatur<{tmp_c:.2f}C,{tmp_f:.2f}F> Luftfeuchtigkeit<{hum_p:.0f}% r.F> Luftdruck<{prs_p:.0f}hPA>'
    csv_header = 'Time;Temperature C;Temperatur F;Humidity r.F;Pressure kPA\n'

    # sensor api object
    bme280 = sensor.BME280('./SensorTest', fmt=sensor_str_format)

    # create console loggin handler
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setFormatter(logging.Formatter(fmt=console_format, datefmt=date_format))
    
    # create csv logging handler
    f_handler = csv_log.FileHandler('tmp.csv', csv_header=csv_header)
    f_handler.setFormatter(csv_log.Formatter(datefmt=date_format, delimiter=';'))
    
    # create logger and set Level
    logger = logging.getLogger("Serverraum_Umweltmanager")
    logger.setLevel(logging.INFO)
    
    # add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    # main loop
    try:
        while(True):
            logger.log(logging.INFO, bme280.get_str_reading(), extra=bme280.get_dict_reading())
            time.sleep(5)
    except KeyboardInterrupt as e:
        print('Programm Interrupted', e)
        sys.exit(0)

if __name__ == '__main__' :
    main()