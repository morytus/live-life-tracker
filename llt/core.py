# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import logging
import click
import json

from llt import Task
from llt import TaskApplication

class Core:
    def load(self):
        @click.group()
        @click.option('--debug', is_flag=True)
        @click.pass_context
        def _cli(ctx, debug:bool):
            if debug == True:
                logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s]: %(message)s')

        _cli.add_command(self.start)
        _cli.add_command(self.stop)
        _cli.add_command(self.restart)
        _cli.add_command(self.status)
        _cli.add_command(self.delete)
        _cli.add_command(self.last)

        _cli(obj={})
        logging.debug(f'mode ON')

    def llt(self, debug:bool):
        pass

    @click.command()
    @click.argument('task')
    @click.option('--category', '-C')
    @click.option('--project', '-P', default='general', show_default=True)
    @click.option('--labels', '-L')
    @click.pass_context
    def start(ctx, category, project, task, labels):
        task = Task(None, category, project, task, labels)
        app = TaskApplication()
        registered = app.register(task)
        click.echo(f'Start task. You\'re great!\n')
        registered.show()
        #if registered.in_progress:
        #    print("YEEEEEEEEEEEES")

    @click.command()
    @click.pass_context
    def stop(ctx):
        app = TaskApplication()
        terminated = app.terminate()
        #click.echo('Stop task.')
        terminated.show()

    @click.command()
    @click.pass_context
    def restart(ctx):
        click.echo('restart!')

    @click.command()
    @click.pass_context
    def status(ctx):
        click.echo('status!')

    @click.command()
    @click.pass_context
    def delete(ctx):
        click.echo(f'Your last task is ...')
        task = Task()

        delete = click.confirm('Delete last task?')
        if delete:
            task.delete()

    @click.command()
    @click.pass_context
    def last(ctx):
        click.echo(f'Your last task is ...')
        task = Task()

def _dump(task:Task) -> str:
    json_str = json.dumps(task.__dict__)
    print(json_str)


#CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#
#if __name__ == "__main__":
#    data = read_tsv(CURRENT_DIR + '/../test/2021-06-15.tsv')
#    print(data)

