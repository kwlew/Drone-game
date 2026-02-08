import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def asset_path(path):
    if isinstance(path, tuple):
        path = os.path.join(*path)  # unpack the tuple
    return os.path.join(BASE_DIR, 'assets', path)