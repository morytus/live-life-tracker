# -*- coding: utf-8 -*-

import json
import click
import inspect
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')

class BaseTask:
    def __init__(
            self, task_id:int = None, category:str = None,
            project:str = None, labels = None, summary:str = None,
            start_time:str = None, end_time:str = None, duration:str = None):

        self.task_id = task_id
        self.category = category
        self.project = project
        self.labels = self._to_list(labels)
        self.summary = summary
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

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

    @property
    def start_ymd(self) -> str:
        start = self.start_time.split('-')
        yyyy = start[0]
        mm = start[1]
        dd = start[2].split(' ')[0]
        return yyyy + mm + dd

    @property
    def uniq_key(self) -> str:
        return f'{self.task_id}-{self.summary}'

    def prepare_start(self):
        if self.start_time is None:
            now = datetime.now().replace(microsecond = 0)
            self.start_time = str(now)

    def prepare_stop(self):
        if self.end_time is None:
            now = datetime.now().replace(microsecond = 0)
            self.end_time = str(now)
        self.duration = self._calc_duration()

    def _to_timestamp(self, target):
        return datetime.strptime(target, '%Y-%m-%d %H:%M:%S')

    def format_start_time(self):
        return self._to_timestamp(self.start_time)

    def format_end_time(self):
        return self._to_timestamp(self.end_time)

    def _calc_duration(self):
        start = self.format_start_time()
        end = self.format_end_time()
        diff = end - start
        return int(diff.total_seconds())

    def show(self, add_lf=False) -> None:
        logging.info(f'   TASK_ID: {self.task_id}')
        logging.info(f'  CATEGORY: {self.category}')
        logging.info(f'   PROJECT: {self.project}')
        logging.info(f'   SUMMARY: {self.summary}')
        logging.info(f'    LABELS: {self.labels}')
        logging.info(f'     START: {self.start_time}')

        if self.end_time:
            logging.info(f'       END: {self.end_time}')
            logging.info(f'  DURATION: {self.duration}')

        if add_lf:
            logging.info('')

    def to_dict(self) -> json:
        return self.__dict__

    def _to_list(self, labels) -> list:
        if type(labels) is list:
            return labels

        if labels:
            return labels.split(',')
        return None


#class Meta(type):
#    def __new__(cls, *args, **kwargs):
#        klass = super().__new__(cls, *args, **kwargs)
#        klass.click_group = click.Group(name=klass.__name__.lower())
#
#        for cmd, cmd_type in inspect.getmembers(klass, lambda x: isinstance(x, click.Command)):
#            type_name = type(cmd_type).__name__.lower()
#            if type_name == 'command':
#                klass.click_group.add_command(cmd_type, cmd)
#
#        return klass
#
#class IBase(metaclass=Meta):
#    pass

