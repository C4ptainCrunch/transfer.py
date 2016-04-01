import warnings

ROOT = "http://partou.se"
MEDIA_DIR = "./media"
SEED_LEN = 5
SECRET = 'nosecret'
DEBUG = False
PORT = 5000

try:
    from local_config import *
except ImportError:
    warnings.warn("No local configuration found", UserWarning)
