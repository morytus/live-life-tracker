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
            project:str = None, summary:str = None, labels = None,
            start_time:str = None, end_time:str = None, duration:str = None):

        super().__init__(task_id, category, project, summary, labels, start_time, end_time, duration)


class TaskFactory:
    def generate(self, task_id, category, project, summary, labels):
        now = datetime.now().replace(microsecond = 0)
        task_id = int(now.timestamp())

        if summary is None:
            app = TaskApplication()
            last = app.last()
            return Task(task_id, last.category, last.project, last.summary, last.labels)

        return Task(task_id, category, project, summary, labels)


class TaskApplication:
    def __init__(self):
        self.repo = TaskRepository()

    def json(self) -> None:
        self.repo.json()

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

        if last.is_finished:
            return None

        result = self.repo.update(last)
        return result

    def remove(self) -> None:
        task = self.repo.last()
        self.repo.delete(task)

    def last(self) -> Task:
        return self.repo.last()


class TaskRepository:
    def __init__(self):
        self.io = IORepository()

    def json(self) -> None:
        self.io.json()

    def insert(self, task:Task) -> Task:
        task.prepare_start()
        self.io.prepare_store(task)
        self.io.insert(task)
        return task

    def update(self, task:Task) -> Task:
        task.prepare_stop()
        self.io.update(task)
        return task

    def delete(self, task:Task) -> None:
        self.io.delete(task)

    def last(self) -> Task:
        last_dict = self.io.last()
        if not last_dict:
            return None

        return Task(**last_dict)

