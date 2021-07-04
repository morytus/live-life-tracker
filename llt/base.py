import click
import inspect
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Base:
    def __init__(self, task_id:int = None, category:str = None,
            project:str = None, summary:str = None, labels = None,
            start_time:str = None, end_time:str = None):

        self.task_id = task_id
        self.category = category
        self.project = project
        self.summary = summary
        self.labels = self._to_list(labels)
        self.start_time = start_time
        self.end_time = end_time

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

    def show(self, add_lf=False):
        logging.info(f'   TASK_ID: {self.task_id}')
        logging.info(f'  CATEGORY: {self.category}')
        logging.info(f'   PROJECT: {self.project}')
        logging.info(f'   SUMMARY: {self.summary}')
        logging.info(f'    LABELS: {self.labels}')
        logging.info(f'     START: {self.start_time}')

        if self.end_time:
            logging.info(f'       END: {self.end_time}')
            logging.info(f'  DURATION: {self.end_time} - {self.start_time}')

        if add_lf:
            logging.info('')

    def _to_list(self, labels) -> list:
        t = type(labels)
        if t is not list:
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

