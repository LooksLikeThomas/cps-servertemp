# Handler for the appending csv file with header
import csv
import io
import logging
import os


class FileHandler(logging.FileHandler):
    def __init__(self, filename, csv_header = None):
        newFile = not os.path.exists(filename)

        super().__init__(filename, mode='a', encoding='utf-8')
        
        if newFile and csv_header:
            self.stream.write(csv_header)

# csv logging formatter
class Formatter(logging.Formatter):
    def __init__(self, datefmt='%Y-%m-%d %H:%M:%S', delimiter = ';'):
        super().__init__(datefmt=datefmt)
        self.output = io.StringIO()
        self.writer = csv.writer(self.output, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)

    def format(self, record):
        self.writer.writerow([record.asctime, record.tmp_c, record.tmp_f, record.hum_p, record.prs_p])
        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()