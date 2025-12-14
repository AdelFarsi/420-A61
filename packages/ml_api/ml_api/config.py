import os

# Version
with open(os.path.join(os.path.dirname(__file__), "VERSION")) as version_file:
    __version__ = version_file.read().strip()

# API settings
DEBUG = True
HOST = "0.0.0.0"
PORT = 5000