# -*- coding: utf-8 -*-

import os
import sys
import time
import toml
import datetime
import logging
import click
import json

from llt import Task
from llt import TaskFactory
from llt import TaskApplication

class Core:
    def __init__(self):
        pass

    @property
    def _output_dir_exists(self) -> bool:
        return True

    def cli(self):
        logging.debug(f'mode ON')

        @click.group()
        @click.option('--debug', is_flag=True)
        @click.pass_context
        def _cli(ctx, debug:bool):
            if debug == True:
                logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s]: %(message)s')

        _cli.add_command(self.register)
        _cli.add_command(self.terminate)
        _cli.add_command(self.remove)
        _cli.add_command(self.last)
        _cli(obj={})

    def llt(self, debug:bool):
        pass

    @click.command('start')
    @click.argument('summary', required=False)
    @click.option('--category', '-C')
    @click.option('--project', '-P', default='general', show_default=True)
    @click.option('--labels', '-L')
    @click.pass_context
    def register(ctx, category, project, summary, labels):
        factory = TaskFactory()
        app = TaskApplication()

        new_task = factory.generate(None, category, project, summary, labels)
        registered = app.register(new_task)

        click.echo(f'Start new task. You\'re great!')
        registered.show()

    @click.command('stop')
    @click.pass_context
    def terminate(ctx):
        app = TaskApplication()
        terminated = app.terminate()
        click.echo('Stop task.')
        terminated.show()

    @click.command('delete')
    @click.pass_context
    def remove(ctx):
        app = TaskApplication()
        click.echo(f'Your last task is ...')
        last = app.last()
        last.show(add_lf=True)

        yes = click.confirm('Delete last task?')
        if yes:
            app.remove()
            click.echo("Delete executed.")

    @click.command('last')
    @click.pass_context
    def last(ctx):
        app = TaskApplication()
        task = app.last()
        if not task:
            click.echo("\nLatest task does not exist.")
            return None

        click.echo("\nLatest task is ...")
        task.show()

def _dump(task:Task) -> str:
    json_str = json.dumps(task.__dict__)
    print(json_str)

