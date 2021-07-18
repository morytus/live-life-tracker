# -*- coding: utf-8 -*-

import os
import toml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    def __init__(self):
        config = self._load_config()
        self.encoding = config['main']['encoding']
        output_dir = config['main']['output_dir']
        publish_dir = config['main']['publish_dir']
        publish_basename = config['main']['publish_basename']

        self.output_dir = self._expanduser(output_dir)
        self.publish_dir = self._expanduser(publish_dir)

        self.publish_path = Path(self.publish_dir, publish_basename)

    def _expanduser(self, target_dir):
        if not target_dir:
            parent_dir = Path.home()
            target_dir = Path(parent_dir, 'llt')

        path = Path(target_dir)
        return str(path.expanduser())

    def _load_config(self) -> dict:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = Path(current_dir, 'config', 'llt.toml')

        if Path(config_file).exists() is False:
            raise Exception(f"Config file '{config_file}' does NOT exist.")

        return toml.load(config_file)

