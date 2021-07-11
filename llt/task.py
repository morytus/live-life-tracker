# -*- coding: utf-8 -*-

import os
import sys
import time
import copy
import json
import logging
from datetime import date
from datetime import datetime
from dataclasses import dataclass
from llt import IORepository
from llt import BaseTask

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task(BaseTask):
    def __init__(self, task_id:int = None, category:str = None,
            project:str = None, summary:str = None, labels = None,
            start_time:str = None, end_time:str = None):

        super().__init__(task_id, category, project, summary, labels, start_time, end_time)


class TaskFactory:
    def generate(self, task_id, category, project, summary, labels):
        now = datetime.now().replace(microsecond = 0)
        task_id = int(now.timestamp())

        if summary is None:
            app = TaskApplication()
            last = app.last()
            return Task(task_id, last.category, last.project, last.summary, last.labels)

        return Task(task_id, category, project, summary, labels)


class TaskService:
    pass


class TaskApplication:
    def __init__(self):
        self.service = TaskService()
        self.repo = TaskRepository()

    def register(self, task:Task) -> Task:
        last = self.repo.last()

        if last and last.in_progress:
            updated = self.repo.update(last)
            logging.info(f'Close last task.')
            updated.show()
            logging.info('')

        result = self.repo.insert(task)

        return result

    def terminate(self) -> Task:
        last = self.repo.last()

        if last.in_progress is False:
            logging.info("Last task ALREADY finished.\n")
            return last

        result = self.repo.update(last)
        logging.info("Task finished NOW.\n")

        return result

    def remove(self) -> None:
        task = self.repo.last()
        self.repo.delete(task)

    def last(self) -> Task:
        return self.repo.last()


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def insert(self, task:Task) -> Task:
        now = datetime.now().replace(microsecond = 0)
        task.start_time = str(now)
        return self.io.insert(task)

    def update(self, task:Task) -> Task:
        now = datetime.now().replace(microsecond = 0)
        task.end_time = str(now)
        return self.io.update(task)

    def delete(self, task:Task) -> None:
        self.io.delete(task)

    def last(self) -> Task:
        last = self.io.last()
        if not last:
            return None

        return Task(**last)

