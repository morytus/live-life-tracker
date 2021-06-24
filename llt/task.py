# -*- coding: utf-8 -*-

import click

class Task():
    def __init__(self):
        click.echo("create instance")

    def add(self):
        click.echo("add called")
