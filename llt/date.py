# -*- coding: utf-8 -*-

from datetime import datetime

class DateValidator:
    def _format(self, target_date:str) -> bool:
        try:
            datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def _sequence(self, start_time:str, end_time:str) -> bool:
        start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if start > end:
            return False
        return True

    def both_date(self, start_time:str, end_time:str) -> bool:
        if not (self._format(start_time) and self._format(end_time)):
            return False

        if not self._sequence(start_time, end_time):
            return False

        return True

