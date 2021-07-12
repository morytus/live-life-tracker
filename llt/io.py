# -*- coding: utf-8 -*-

import os
import json
import pprint
import logging
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

    def insert(self, task) -> None:
        parent_path = PurePath(self.output_dir, task.start_ymd)

        if parent_path.exists() is False:
            parent_path.mkdir(parents=True, exist_ok=True)

        file_name = task.file_key + '-' + task.summary + '.json'
        output_file = PurePath(parent_path, file_name)
        task_dict = task.to_dict()

        with open(output_file, "w", encoding=self.encoding) as f:
            json.dump(task_dict, f, ensure_ascii=False)

    def update(self, task) -> None:
        parent_path = PurePath(self.output_dir, task.start_ymd)

        file_name = task.file_key + '-' + task.summary + '.json'
        output_file = PurePath(parent_path, file_name)
        task_dict = task.to_dict()

        with open(output_file, "w", encoding=self.encoding) as f:
            json.dump(task_dict, f, ensure_ascii=False)

    def delete(self, task) -> None:
        pass

    def last(self) -> dict:
        last_file = self._latest_path(self.output_dir)
        logging.info(f"last_file: {last_file}")
        if not last_file:
            return None

        return self._to_dict(last_file)


    def _to_dict(self, file_path) -> dict:
        with open(file_path, "r", encoding=self.encoding) as f:
            data = json.load(f)

        return data

    def _latest_path(self, target_path) -> str:
        path = Path(target_path)
        if not path.exists():
            return None

        paths = sorted([str(p) for p in path.iterdir()])
        if not paths:
            return None

        last_path = paths[-1]
        if Path(last_path).is_file():
            return last_path

        return self._latest_path(last_path)


class DummyTask(BaseTask):
    def __init__(self):
        self.task_id = "1234567890"
        self.category = "Nice Category"
        self.project = "Awesome Project"
        self.summary = "Good Task"
        self.labels = self._to_list("111,222,333")
        self.start_time = datetime.strptime("2021-06-27 12:34:56", "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.now().replace(microsecond = 0)

