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


class TaskApplication:
    def __init__(self):
        self.task_factory = TaskFactory()
        self.task_repo = TaskRepository()
        self.task_service = TaskService()
        self.now = datetime.now().replace(microsecond = 0)

    def find(self) -> Task:
        pass

    def register(self, task:Task) -> Task:
        return self.task_repo.insert(task)

    def terminate(self) -> Task:
        last_task = self.task_service.last()
        if last_task.in_progress:
            last_task.end_time = str(self.now)
            last_task = self.task_repo.update(last_task)
            logging.info("Task finished NOW.\n")
        else:
            logging.info("Last task ALREADY finished.\n")
        return last_task

    def remove(self) -> None:
        last_task = self.task_service.last()
        self.task_repo.delete(last_task)


class TaskFactory:
    def generate(self, task_id, category, project, summary, labels):

        now = datetime.now().replace(microsecond = 0)
        task_id = int(now.timestamp())
        start_time = str(now)

        if summary is None:
            logging.info("New task will generate from last!")
            return Task(task_id, category, project, summary, labels)

        return Task(task_id, category, project, summary, labels)

class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()
        self.now = datetime.now().replace(microsecond = 0)

    def generate(self, task) -> Task:
        pass

    def is_finished(self) -> bool:
        last_task = self.last()
        return last_task.is_finished

    def in_progress(sef) -> bool:
        last_task = self._last()
        return last_task.in_progress

    def last(self) -> Task:
        #+# select last_task
        return self.task_repo.select(None)

    def is_first(self):
        # try to register first task
        pass

    def _has_body(self):
        # True when not only file header
        pass


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def insert(self, task:Task) -> Task:
        return self.io.insert(task)

    def select(self, task:Task) -> Task:
        return self.io.select(task)

    def update(self, task:Task) -> Task:
        return self.io.update(task)

    def delete(self, task:Task) -> None:
        self.io.delete(task)

