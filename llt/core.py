# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import logging
import click
from llt import Task

class Core:
    def load(self):
        @click.group()
        @click.option('--debug', is_flag=True)
        @click.pass_context
        def _cli(ctx, debug):
            if debug is True:
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

    def llt(self, debug):
        pass

    @click.command()
    @click.argument('task')
    @click.option('--category', '-c')
    @click.option('--project', '-p', default='general', show_default=True)
    @click.option('--labels', '-l')
    @click.pass_context
    def start(ctx, task, category, project, labels):
        task = Task(task, category, project, labels)
        task.add()

        click.echo(f'Start task. You\'re great!\n')
        task.last()

    @click.command()
    @click.pass_context
    def stop(ctx):
        click.echo('Stop task.')

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
        task.last()

        delete = click.confirm('Delete last task?')
        if delete:
            task.delete()

    @click.command()
    @click.pass_context
    def last(ctx):
        click.echo(f'Your last task is ...')
        task = Task()
        task.last()

#CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#
#if __name__ == "__main__":
#    data = read_tsv(CURRENT_DIR + '/../test/2021-06-15.tsv')
#    print(data)

