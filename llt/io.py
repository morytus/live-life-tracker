# -*- coding: utf-8 -*-

import os
import sys
import json
import pprint
from pathlib import Path
from pathlib import PurePath
from datetime import datetime
from llt import BaseTask
from llt import Config

class IORepository:
    def __init__(self):
        config = Config()
        self.encoding = config.encoding
        self.output_dir = config.output_dir

    def insert(self, task):
        path = Path(self.output_dir + '/' + task.start_ymd)

        if path.exists() is False:
            path.mkdir(parents=True, exist_ok=True)

        file_name = task.file_key + '-' + task.summary + '.json'
        output_file = PurePath(str(path), file_name)
        task_dict = task.to_dict()

        with open(output_file, "w", encoding=self.encoding) as f:
            json.dump(task_dict, f, ensure_ascii=False)

        return task

    def update(self, task):
        path = Path(self.output_dir + '/' + task.start_ymd)
        file_name = task.file_key + '-' + task.summary + '.json'
        output_file = PurePath(str(path), file_name)
        task_dict = task.to_dict()

        with open(output_file, "w", encoding=self.encoding) as f:
            json.dump(task_dict, f, ensure_ascii=False)

    def delete(self, task):
        pass

    def last(self):
        last_dir = self._latest_path(self.output_dir)
        if not last_dir:
            return None

        last_file = self._latest_path(last_dir)
        return self._to_dict(last_file)


    def _to_dict(self, file_path):
        with open(file_path, "r", encoding=self.encoding) as f:
            data = json.load(f)

        return data

    def _latest_path(self, target_dir):
        path = Path(target_dir)
        if not path.exists():
            return None

        paths = sorted([str(p) for p in path.iterdir()])
        if not paths:
            return None

        return paths[-1]

    def _read(self):
        data = []
        idx = 0
        #with open(filepath, "r", encoding=self.encoding) as f:
        #    reader = csv.reader(f, delimiter='\t')
        #    for row in reader:
        #        data.append(row)
        return data


class DummyTask(BaseTask):
    def __init__(self):
        self.task_id = "1234567890"
        self.category = "Nice Category"
        self.project = "Awesome Project"
        self.summary = "Good Task"
        self.labels = self._to_list("111,222,333")
        self.start_time = datetime.strptime("2021-06-27 12:34:56", "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.now().replace(microsecond = 0)

