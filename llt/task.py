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
from llt import Base

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task(Base):
    def __init__(self, task_id:int = None, category:str = None,
            project:str = None, summary:str = None, labels:str = None,
            start_time:str = None, end_time:str = None):

        super().__init__(task_id, category, project, summary, labels, start_time, end_time)


class TaskFactory:
    def generate(self, task_id, category, project, summary, labels):
        now = datetime.now().replace(microsecond = 0)
        task_id = int(now.timestamp())
        start_time = str(now)

        if summary is None:
            logging.info("New task will generate from last!")

            # ----------------------------
            # TODO: retrieve latest task
            # ----------------------------

            return Task(task_id, category, project, summary, labels, start_time)

        return Task(task_id, category, project, summary, labels, start_time)


class TaskTweek:
    def __init__(self):
        self.repo = TaskRepository()
        self.now = datetime.now().replace(microsecond = 0)

    def is_finished(self) -> bool:
        last_task = self.last()
        return last_task.is_finished

    def in_progress(sef) -> bool:
        last_task = self._last()
        return last_task.in_progress

    def last(self) -> Task:
        #+# select last_task
        return self.status(None)

    def _is_first(self):
        # try to register first task
        pass

    def _has_body(self):
        # True when not only file header
        pass


class TaskService:
    def __init__(self):
        self.tweek = TaskTweek()
        self.repo = TaskRepository()
        self.now = datetime.now().replace(microsecond = 0)

    def register(self, task:Task) -> Task:
        task = self.repo.latest()

        if task.in_progress:
            task.end_time = str(self.now)
            task = self.repo.update(task)

        result = self.repo.insert(task)
        logging.info(f'Start task. You\'re great!\n')

        return result

    def terminate(self) -> Task:
        task = self.repo.latest()

        if task.in_progress is False:
            logging.info("Last task ALREADY finished.\n")
            return task

        task.end_time = str(self.now)
        result = self.repo.update(task)
        logging.info("Task finished NOW.\n")

        return result

    def remove(self) -> None:
        task = self.repo.latest()
        self.repo.delete(task)

    def status(self) -> Task:
        return self.repo.latest(task)


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def insert(self, task:Task) -> Task:
        return self.io.insert(task)

    def update(self, task:Task) -> Task:
        return self.io.update(task)

    def delete(self, task:Task) -> None:
        self.io.delete(task)

    def latest(self) -> Task:
        return self.io.latest()

