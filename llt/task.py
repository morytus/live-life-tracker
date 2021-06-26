# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import date
from datetime import datetime
import os
import sys
import time
import copy
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task:
    def __init__(self, task_id:int = None, category:str = None,
            project:str = None, task:str = None, labels:str = None,
            start_time:str = None, end_time:str = None):

        self.task_id = task_id
        self.category = category
        self.project = project
        self.task = task
        self.labels = self._to_list(labels)
        self.start_time = start_time
        self.end_time = end_time

    def show(self):
        logging.info(f'   TASK_ID: {self.task_id}')
        logging.info(f'  CATEGORY: {self.category}')
        logging.info(f'   PROJECT: {self.project}')
        logging.info(f'      TASK: {self.task}')
        logging.info(f'    LABELS: {self.labels}')
        logging.info(f'     START: {self.start_time}')
        if self.end_time:
            logging.info(f'       END: {self.end_time}')
            logging.info(f'  DURATION: {self.end_time} - {self.start_time}')

    @property
    def is_finished(self) -> bool:
        if self.start_time and self.end_time:
            return True

    def _to_list(self, labels:str) -> list:
        return labels.split(',')


class TaskApplication:
    def __init__(self):
        self.task_service = TaskService()
        self.task_repo = TaskRepository()

    def register(self, task:Task) -> Task:
        now = datetime.now().replace(microsecond = 0)

        entity = copy.deepcopy(task)
        entity.task_id = int(now.timestamp())
        entity.start_time = str(now)

        self.task_repo.save(entity)
        return entity

    def terminate(self) -> Task:
        last_task = task_service.last()
        if last_task.is_finished:
            logging.info("finished")
        return task


class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()

    def last(self) -> Task:
        task = self.task_repo.last()
        return task


class TaskRepository:
    def __init__(self):
        pass

    def save(self, task:Task) -> None:
        pass

    def find(self, task:Task) -> Task:
        pass

    def last(self) -> Task:
        pass

    def modify(self, task:Task):
        pass


class File:
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


