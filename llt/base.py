import click
import inspect

class Meta(type):
    def __new__(cls, *args, **kwargs):
        klass = super().__new__(cls, *args, **kwargs)
        klass.click_group = click.Group(name=klass.__name__.lower())

        for cmd, cmd_type in inspect.getmembers(klass, lambda x: isinstance(x, click.Command)):
            type_name = type(cmd_type).__name__.lower()
            if type_name == 'command':
                klass.click_group.add_command(cmd_type, cmd)

        return klass

class Base(metaclass=Meta):
    pass

