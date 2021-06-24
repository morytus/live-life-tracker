# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import csv
import click
from llt.task import Task

class Core():
    def __init__(self):
        click.echo("create instance")

    @click.group()
    @click.option('--debug', is_flag=True)
    @click.pass_context
    def cmd(self, ctx, debug):
        llt(debug)
        task = Task()
        #ctx.debug = debug
        #ctx.task = task

    def llt(self, debug):
        pass

    @cmd.command()
    @click.argument('task')
    @click.option('--category', '-c')
    @click.option('--project', '-p', default='general', show_default=True)
    @click.option('--labels', '-l')
    def start(self, task, category, project, labels):
        click.echo(f'Start task. You\'re great!\n CATEGORY: {category}\n  PROJECT: {project}\n     TASK: {task}\n   LABELS: {labels}')

    @cmd.command()
    def stop(self):
        click.echo('stop!')

    @cmd.command()
    def restart(self):
        click.echo('restart!')

    @cmd.command()
    def echo(self):
        click.echo('echo!')

    @cmd.command()
    def delete(self):
        category = 'woo'
        project = 'yah'
        task = 'tah'
        labels = 'hoo'

        click.echo(f'Your last task is ...\n CATEGORY: {category}\n  PROJECT: {project}\n     TASK: {task}\n   LABELS: {labels}\n')
        delete = click.prompt('Delete last task?', type=str, default='no')
        click.echo('delete?: {}'.format(delete))

    def last_task(self):
        click.echo("last task!")

def read_tsv(filename):
    data = []
    idx = 0
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            data.append(row)
    return data

def write_record(filename, record):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(record)

def validate_file():
    pass

def start_task():
    pass

def stop_task():
    pass

def restart_task():
    pass

def calc_duration():
    pass

def what_time():
    now = datetime.datetime.now()
    return f"{now:%Y-%m-%d %H:%M:%S}"

def echo_message():
    pass

def add_category():
    pass

def add_project():
    pass

def add_tag():
    pass

def validate_file(filename):
    ## True
    # 存在しない
    # 最終レコードを除く全レコードのカラム数が7
    # 最終レコードのカラム数が5，または7
    ## False
    # 上記のいずれでもない
    pass

def count_cols():
    pass

def count_rows():
    pass

def create_header():
    pass

def is_debug(debug_flag):
    if debug_flag:
        return True

#CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#
#if __name__ == "__main__":
#    data = read_tsv(CURRENT_DIR + '/../test/2021-06-15.tsv')
#    print(data)

