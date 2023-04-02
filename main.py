#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

import os
import yaml
from database import Database

CONFIG_FILEPATH = os.path.realpath(os.path.dirname(__file__)) + "/config.yml"

class Application:
    def __init__(self):
        # Loading global configuration
        self.config_file = CONFIG_FILEPATH
        self.load_config()

        # Database object
        self.db = Database(self.config['database'])

    def load_config(self):
        with open(self.config_file) as f:
            self.config = yaml.safe_load(f)

def main():
    app = Application()

if __name__ == "__main__":
    main()
