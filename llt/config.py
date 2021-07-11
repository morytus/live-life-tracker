# -*- coding: utf-8 -*-

import os
import sys
import toml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    def __init__(self):
        config = self._load_config()
        self.encoding = config['main']['encoding']
        output_dir = config['main']['output_dir']

        if not output_dir:
            parent_dir = Path.home()
            output_dir = str(parent_dir) + '/llt'

        path = Path(output_dir)
        self.output_dir = str(path.expanduser())

    def _load_config(self) -> dict:
        config_file = os.path.dirname(os.path.abspath(__file__)) + '/config/llt.toml'

        if os.path.exists(config_file) is False:
            raise Exception(f"Config file '{config_file}' does NOT exist.")

        return toml.load(config_file)

