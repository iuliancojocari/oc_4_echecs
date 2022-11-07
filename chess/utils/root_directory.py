from pathlib import Path
import os

file = __file__



def get_root_dir():

    root_dir = os.path.dirname(__file__)
    BASE_DIR = os.path.dirname(root_dir)

    return BASE_DIR


