import os

import yaml


def parse_settings(filename='./settings.yaml'):

    if not os.path.exists(filename):
        print('File does not exist:', filename)
        quit()
    
    print('Using for settings: ', filename)

    with open(filename) as f:
        return yaml.safe_load(f)