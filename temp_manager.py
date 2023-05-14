# CPS Serverraumsteuerung

import sys
import sensor
import logging
import time
import csv_log

def main():
    bme280 = sensor.BME280('./SensorTest')

    # console formatter
    date_format = '%Y-%m-%d %H:%M:%S'
    console_format = '%(asctime)s - %(name)s - %(msg)s'
    csv_header = 'Time;Temperature C;Temperatur F;Humidity r.F;Pressure hPA\n'

    # create console loggin handler
    c_handler = console_handler(console_format, date_format)
    
    # create csv logging handler
    f_handler = csv_handler(csv_header)

    # create logger and set Level
    logger = logging.getLogger("temp_manager")
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


def console_handler(fmt, datefmt):
    # create formatter
    console_formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    # create handler
    c_handler = logging.StreamHandler(sys.stdout)

    # add formatter to handler and return
    c_handler.setFormatter(console_formatter)
    return c_handler


def csv_handler(csv_header):
    # create fromatter
    csv_formatter = csv_log.Formatter(delimiter=';')

    # create handler
    f_handler = csv_log.FileHandler('tmp.csv', csv_header=csv_header)

    # add formatter to handler and return
    f_handler.setFormatter(csv_formatter)
    return f_handler

if __name__ == '__main__' :
    main()