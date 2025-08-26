from yarnspawner.spawner import YarnSpawner

# Register apihandler
from . import apihandler
del apihandler

from . import _version
__version__ = _version.get_versions()['version']
