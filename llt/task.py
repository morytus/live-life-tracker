# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import date
from datetime import datetime
import os
import sys
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task:
    category: str = None
    project: str = None
    task: str = None
    labels: list = None
    start: datetime = datetime.now()
    end: datetime = None

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    def delete(self):
        pass

    def status(self):
        pass

    def last(self):
        logging.info(f'  CATEGORY: {self.category}')
        logging.info(f'   PROJECT: {self.project}')
        logging.info(f'      TASK: {self.task}')
        logging.info(f'    LABELS: {self.labels}')
        logging.info(f'     START: {self.start}')
        if self.end:
            logging.info(f'       END: {self.end}')
            logging.info(f'  DURATION: {self.end} - {self.start}')

    def validate(self):
        pass


class File:
    def __init__(self, filepath, encoding):
        self.filepath = filepath
        self.encoding = encoding

    def validate(self):
        # True
        ## is Not exists
        ## or columns count is 5 ro 7
        pass

    def read(self):
        data = []
        idx = 0
        with open(filename, "r", encoding=self.encoding) as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                data.append(row)
        return data

    def write(self, record):
        with open(filename, "a", encoding=self.encoding) as f:
            f.write(record)

    def count_cols():
        pass

    def count_rows():
        pass

    def create_header():
        pass


