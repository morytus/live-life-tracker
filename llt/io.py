# -*- coding: utf-8 -*-

import os
import glob
import json
import logging
import fileinput
from pathlib import Path
from pprint import pprint
from datetime import datetime
from llt import BaseTask
from llt import Config

logging.basicConfig(level=logging.INFO, format='%(message)s')

class IORepository:
    def __init__(self):
        config = Config()
        self.encoding = config.encoding
        self.output_dir = config.output_dir

    def prepare_store(self, task) -> None:
        parent_path = Path(self.output_dir, task.start_ymd)
        if Path(parent_path).exists() is False:
            parent_path.mkdir(parents=True, exist_ok=True)

    def json(self,) -> None:
        config = Config()
        path = Path(config.output_dir).expanduser()

        files = glob.glob(str(path) + "/**/*")
        publish_path = Path(str(config.publish_path) + '.json')
        #pprint(files)

        if files:
            with open(publish_path, 'w', encoding=config.encoding) as fp:
                with fileinput.input(files) as ff:
                    fp.write('[\n')
                    for line in ff:
                        if ff.lineno() == 1:
                            fp.write(f'{line}\n')
                            continue

                        fp.write(f', {line}\n')
                    fp.write(']')


    def insert(self, task) -> None:
        self._upsert(task)

    def update(self, task) -> None:
        self._upsert(task)

    def last(self) -> dict:
        last_file = self._last_file_from(self.output_dir)
        if not last_file:
            return None
        return self._to_dict(last_file)

    def _upsert(self, task) -> None:
        file_name = task.uniq_key + '.json'
        output_file = Path(self.output_dir, task.start_ymd, file_name)

        task_dict = task.to_dict()
        with open(output_file, "w", encoding=self.encoding) as f:
            json.dump(task_dict, f, ensure_ascii=False)

    def _to_dict(self, file_path) -> dict:
        with open(file_path, "r", encoding=self.encoding) as f:
            data = json.load(f)
        return data

    def _last_file_from(self, search_path) -> str:
        path = Path(search_path)
        if not path.exists():
            return None

        paths = sorted([str(p) for p in path.iterdir()])
        if not paths:
            return None

        target_path = paths[-1]
        if Path(target_path).is_file():
            return target_path

        return self._last_file_from(target_path)


class DummyTask(BaseTask):
    def __init__(self):
        self.task_id = "1234567890"
        self.category = "Nice Category"
        self.project = "Awesome Project"
        self.summary = "Good Task"
        self.labels = self._to_list("111,222,333")
        self.start_time = datetime.strptime("2021-06-27 12:34:56", "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.now().replace(microsecond = 0)

