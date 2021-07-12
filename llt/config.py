# -*- coding: utf-8 -*-

import os
import toml
from pathlib import Path
from pathlib import PurePath
from dataclasses import dataclass

@dataclass
class Config:
    def __init__(self):
        config = self._load_config()
        self.encoding = config['main']['encoding']
        output_dir = config['main']['output_dir']

        if not output_dir:
            parent_dir = Path.home()
            output_dir = PurePath(parent_dir, 'llt')

        path = Path(output_dir)
        self.output_dir = str(path.expanduser())

    def _load_config(self) -> dict:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = PurePath(current_dir, 'config', 'llt.toml')

        if Path(config_file).exists() is False:
            raise Exception(f"Config file '{config_file}' does NOT exist.")

        return toml.load(config_file)

