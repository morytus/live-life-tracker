# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from dataclasses import dataclass
from llt import IORepository
from llt import BaseTask
from llt.date import build_today

logging.basicConfig(level=logging.INFO, format='%(message)s')

@dataclass
class Task(BaseTask):
    def __init__(
            self, task_id:int = None, category:str = None,
            project:str = None, labels = None, summary:str = None,
            start_time:str = None, end_time:str = None, duration:str = None):

        super().__init__(task_id, category, project, labels, summary, start_time, end_time, duration)


class TaskFactory:
    def create(
            self, category, project, labels, summary, is_today=False,
            start_time=None, end_time=None):

        if is_today:
            start_time = build_today(start_time)
            end_time = build_today(end_time)

        task_id = self._generate_id_from(start_time)

        if summary is None:
            app = TaskApplication()
            last = app.last()
            return Task(task_id, last.category, last.project, last.labels, last.summary)
        return Task(task_id, category, project, labels, summary, start_time, end_time)

    def _generate_id_from(self, start_time):
        if start_time is None:
            now = datetime.now().replace(microsecond = 0)
            return int(now.timestamp())
        return int(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timestamp())


class TaskApplication:
    def __init__(self):
        self.repo = TaskRepository()

    def json(self) -> None:
        self.repo.json()

    def register(self, reg_task:Task) -> Task:
        last_task = self.repo.last()
        if last_task.in_progress and self._is_sequential(last_task, reg_task):
            self._terminate(last_task)

        reg_task.prepare_stop()
        return self._generate(reg_task)

    def start(self, task:Task) -> Task:
        last_task = self.repo.last()
        if last_task.in_progress:
            self._terminate(last_task)

        task.prepare_start()
        return self._generate(task)

    def stop(self) -> Task:
        last_task = self.repo.last()
        if last_task.is_finished:
            return None
        return self._terminate(last_task)

    def _to_timestamp(self, target_date) -> datetime:
        return datetime.strptime(target_date.start_time, '%Y-%m-%d %H:%M:%d')

    def _is_sequential(self, pre, post) -> bool:
        pre_time = pre.format_start_time()
        post_time = post.format_start_time()
        if pre_time < post_time:
            return True
        return False

    def _generate(self, task) -> Task:
        return self.repo.insert(task)

    def _terminate(self, task) -> Task:
        task.prepare_stop()
        result = self.repo.update(task)
        logging.info(f'Closed last task.')
        result.show()
        logging.info('')
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

