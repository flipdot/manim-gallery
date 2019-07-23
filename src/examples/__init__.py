from os.path import dirname, basename, isfile, join
import glob
from pathlib import Path

modules = glob.glob(join(dirname(__file__), '**/*.py'), recursive=True)
# __all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.startswith('_')]
paths = [Path(x) for x in modules]
__all__ = [f'{p.parent.name}.{p.stem}' for p in paths if p.is_file() and not p.name.startswith('_') and p.parent.name != 'examples']
