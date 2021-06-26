# -*- coding: utf-8 -*-

import click
from llt import Core

#@click.group()
#@click.pass_context
#def cli(ctx):
#    ctx.obj = {'uno': 1}
#    click.echo(f'ctx: {ctx}')
#
#@cli.command()
#@click.pass_context
#def woo(ctx):
#    click.echo(f'ctx: {ctx}')
#    click.echo(f'ctx: {ctx.obj["uno"]}')

def main():
    core = Core()

    #cli.add_command(core.start)
    #cli.add_command(core.stop)
    cli(obj={})

if __name__ == '__main__':
    main()

