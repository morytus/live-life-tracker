# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from dataclasses import dataclass
from llt import IORepository
from llt import BaseTask

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task(BaseTask):
    def __init__(
            self, task_id:int = None, category:str = None,
            project:str = None, labels = None, summary:str = None,
            start_time:str = None, end_time:str = None, duration:str = None):

        super().__init__(task_id, category, project, labels, summary, start_time, end_time, duration)


class TaskFactory:
    def generate(
            self, task_id, category, project, labels,
            summary, start_time=None, end_time=None):

        now = datetime.now().replace(microsecond = 0)
        task_id = int(now.timestamp())

        if summary is None:
            app = TaskApplication()
            last = app.last()
            return Task(task_id, last.category, last.project, last.labels, last.summary)

        return Task(task_id, category, project, labels, summary, start_time, end_time)


class TaskApplication:
    def __init__(self):
        self.repo = TaskRepository()

    def json(self) -> None:
        self.repo.json()

    def register(self, task:Task) -> Task:
        task.prepare_start()
        task.prepare_stop()
        result = self.repo.insert(task)
        return result

    def start(self, task:Task) -> Task:
        last = self.repo.last()

        if last and last.in_progress:
            last.prepare_stop()
            updated = self.repo.update(last)
            logging.info(f'Closed last task.')
            updated.show()
            logging.info('')

        task.prepare_start()
        result = self.repo.insert(task)
        return result

    def stop(self) -> Task:
        last = self.repo.last()

        if last.is_finished:
            return None

        last.prepare_stop()
        result = self.repo.update(last)
        return result

    def last(self) -> Task:
        return self.repo.last()


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def json(self) -> None:
        self.io.json()

    def insert(self, task:Task) -> Task:
        self.io.prepare_store(task)
        self.io.insert(task)
        return task

    def update(self, task:Task) -> Task:
        self.io.update(task)
        return task

    def last(self) -> Task:
        last_dict = self.io.last()
        if not last_dict:
            return None

        return Task(**last_dict)

