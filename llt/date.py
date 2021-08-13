# -*- coding: utf-8 -*-

from datetime import datetime

class DateValidator:
    def __init__(self, is_today):
        self.is_today = is_today

    def format(self, target_date:str) -> bool:
        try:
            datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def sequence(self, start_time:str, end_time:str) -> bool:
        start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if start > end:
            return False
        return True

    def both_date(self, start_time:str, end_time:str) -> bool:
        if self.is_today:
            start_time = build_today(start_time)
            end_time = build_today(end_time)

        if not (self.format(start_time) and self.format(end_time)):
            return False

        if not self.sequence(start_time, end_time):
            return False

        return True

def build_today(target_date:str) -> str:
    _list = target_date.split(' ')

    if len(_list) == 2:
        time_part = _list[1]
    else:
        time_part = _list[0]

    return f'{datetime.now():%Y-%m-%d}' + ' ' + time_part

