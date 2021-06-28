# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import logging
import click
import json

from llt import Task
from llt import TaskFactory
from llt import TaskApplication

class Core:
    def load(self):
        logging.debug(f'mode ON')

        @click.group()
        @click.option('--debug', is_flag=True)
        @click.pass_context
        def _cli(ctx, debug:bool):
            if debug == True:
                logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s]: %(message)s')

        _cli.add_command(self.start)
        _cli.add_command(self.stop)
        _cli.add_command(self.delete)
        _cli.add_command(self.status)
        _cli(obj={})

    def llt(self, debug:bool):
        pass

    @click.command()
    @click.argument('summary', required=False)
    @click.option('--category', '-C')
    @click.option('--project', '-P', default='general', show_default=True)
    @click.option('--labels', '-L')
    @click.pass_context
    def start(ctx, category, project, summary, labels):
        # check out that other task is in progress

        factory = TaskFactory()
        app = TaskApplication()

        new_task = factory.generate(None, category, project, summary, labels)
        registered = app.register(new_task)
        click.echo(f'Start task. You\'re great!\n')
        registered.show()

    @click.command()
    @click.pass_context
    def stop(ctx):
        app = TaskApplication()
        terminated = app.terminate()
        click.echo('Stop task.')
        terminated.show()

    @click.command()
    @click.pass_context
    def delete(ctx):
        click.echo(f'Your last task is ...')

        delete = click.confirm('Delete last task?')
        if delete:
            app = TaskApplication()
            app.remove()
            click.echo("Delete executed.")

    @click.command()
    @click.pass_context
    def status(ctx):
        click.echo('status!')
        # print last task if exists

def _dump(task:Task) -> str:
    json_str = json.dumps(task.__dict__)
    print(json_str)


#CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#
#if __name__ == "__main__":
#    data = read_tsv(CURRENT_DIR + '/../test/2021-06-15.tsv')
#    print(data)

