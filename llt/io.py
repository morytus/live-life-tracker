import os
import sys

class IORepository:
    def __init__(self):
        # TODO: Parameters bind to config file
        self.fo = FileRepository('~/work/output.json', 'utf-8')

    def save(self, task) -> None:
        return DummyTask()

    def find(self, task):
        return DummyTask()

    def last(self):
        return DummyTask()

    def modify(self, task):
        return DummyTask()


class FileRepository:
    def __init__(self, filepath:str, encoding:str):
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

    def write(self, record:str):
        with open(filename, "a", encoding=self.encoding) as f:
            f.write(record)

    def count_cols():
        pass

    def count_rows():
        pass

    def create_header():
        pass


class DummyTask():
    def __init__(self):
        self.task_id = "1234567890"
        self.category = "Nice Category"
        self.project = "Awesome Project"
        self.task = "Good Task"
        self.labels = self._to_list("111,222,333")
        self.start_time = "2021-06-27 12:34:35"
        self.end_time = None

    @property
    def is_finished(self) -> bool:
        if self.start_time and self.end_time:
            return True
        return False

    @property
    def in_progress(self) -> bool:
        if self.start_time and not self.end_time:
            return True
        return False

    def _to_list(self, labels:str) -> list:
        return labels.split(',')

