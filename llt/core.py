# -*- coding: utf-8 -*-

import click
import logging
from llt import Task
from llt import TaskFactory
from llt import TaskApplication

logging.basicConfig(level=logging.INFO, format='%(message)s')

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

        _cli.add_command(self.json)
        _cli.add_command(self.start)
        _cli.add_command(self.stop)
        _cli.add_command(self.last)
        _cli(obj={})

    def llt(self, debug:bool):
        pass

    @click.command('json')
    @click.pass_context
    def json(ctx):
        app = TaskApplication()
        app.json()

    @click.command('reg')
    @click.argument('summary', required=False)
    @click.option('--category', '-C')
    @click.option('--project', '-P', default='General', show_default=True)
    @click.option('--labels', '-L')
    @click.pass_context
    def register(ctx):
        pass

    @click.command('start')
    @click.argument('summary', required=False)
    @click.option('--category', '-C')
    @click.option('--project', '-P', default='General', show_default=True)
    @click.option('--labels', '-L')
    @click.pass_context
    def start(ctx, category, project, summary, labels):
        factory = TaskFactory()
        app = TaskApplication()

        new_task = factory.generate(None, category, project, summary, labels)
        started = app.start(new_task)

        click.echo(f'Start new task. You\'re great!')
        started.show()

    @click.command('stop')
    @click.pass_context
    def stop(ctx):
        app = TaskApplication()
        stopped = app.stop()
        if stopped:
            click.echo('Stop task.')
            stopped.show()
        else:
            logging.info("Last task ALREADY finished.")

    @click.command('last')
    @click.pass_context
    def last(ctx):
        app = TaskApplication()
        task = app.last()
        if not task:
            click.echo("Last task does not exist.")
            return None

        click.echo("Last task is ...")
        task.show()


def _dump(task:Task) -> str:
    json_str = json.dumps(task.__dict__)
    print(json_str)

