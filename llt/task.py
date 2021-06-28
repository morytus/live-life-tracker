# -*- coding: utf-8 -*-

import os
import sys
import time
import copy
import logging
from datetime import date
from datetime import datetime
from dataclasses import dataclass
from llt import IORepository

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
        return False

    @property
    def in_progress(self) -> bool:
        if self.start_time and not self.end_time:
            return True
        return False

    def _to_list(self, labels:str) -> list:
        return labels.split(',')


class TaskApplication:
    def __init__(self):
        self.task_service = TaskService()
        self.task_repo = TaskRepository()
        self.now = datetime.now().replace(microsecond = 0)

    def register(self, task:Task) -> Task:
        entity = copy.deepcopy(task)
        entity.task_id = int(self.now.timestamp())
        entity.start_time = str(self.now)

        self.task_repo.save(entity)
        return entity

    def terminate(self) -> Task:
        last = self.task_repo.last()
        if last.in_progress:
            last.end_time = str(self.now)
            last = self.task_repo.modify(last)
            logging.info("Task NOW finished.")
        else:
            logging.info("Last task ALREADY finished.")

        return last


class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()

    def is_finished(self) -> bool:
        last = self.task_repo.last()
        return last.is_finished

    def in_progress(sef) -> bool:
        last = self.task_repo.last()
        return last.in_progress

    def last(self) -> Task:
        last = self.task_repo.last()
        return last

    def _has_body(self):
        # True when not only header
        pass


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def save(self, task:Task) -> None:
        self.io.save(task)

    def find(self, task:Task) -> Task:
        return self.io.find(task)

    def last(self) -> Task:
        return self.io.last()

    def modify(self, task:Task) -> Task:
        return self.io.modify(task)


