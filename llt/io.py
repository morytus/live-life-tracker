import os
import sys
from llt import Base

#+# -----------------------------------------------
#+# TODO: Add file io for recording
#+# -----------------------------------------------

class IORepository:
    def __init__(self):
        self.filepath = '~/work/output.json'
        self.encoding = 'utf-8'

    def insert(self, task):
        return task

    def update(self, task):
        return DummyTask()

    def delete(self, task):
        pass

    def last(self):
        return DummyTask()

    def validate(self):
        # True
        ## is Not exists
        ## or columns count is 5 ro 7
        pass

    def read(self):
        data = []
        idx = 0
        with open(filepath, "r", encoding=self.encoding) as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                data.append(row)
        return data

    def write(self, record):
        with open(filepath, "a", encoding=self.encoding) as f:
            f.write(record)

    def count_cols():
        pass

    def count_rows():
        pass

    def create_header():
        pass


class DummyTask(Base):
    def __init__(self):
        self.task_id = "1234567890"
        self.category = "Nice Category"
        self.project = "Awesome Project"
        self.summary = "Good Task"
        self.labels = self._to_list("111,222,333")
        self.start_time = "2021-06-27 12:34:56"
        self.end_time = None

