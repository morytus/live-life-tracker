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
from llt import TaskService

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

        _cli.add_command(self.register)
        _cli.add_command(self.terminate)
        _cli.add_command(self.remove)
        _cli.add_command(self.status)
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
        service = TaskService()

        new_task = factory.generate(None, category, project, summary, labels)
        registered = service.register(new_task)

        click.echo(f'Start task. You\'re great!\n')
        registered.show()

    @click.command('stop')
    @click.pass_context
    def terminate(ctx):
        service = TaskService()
        terminated = service.terminate()
        click.echo('Stop task.')
        terminated.show()

    @click.command('delete')
    @click.pass_context
    def remove(ctx):
        click.echo(f'Your last task is ...')

        yes = click.confirm('Delete last task?')
        if yes:
            service = TaskService()
            service.remove()
            click.echo("Delete executed.")

    @click.command('status')
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

