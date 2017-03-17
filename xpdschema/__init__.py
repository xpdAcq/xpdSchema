import json
from enum import Enum
from pkg_resources import resource_filename as rs_fn


__all__ = ['DocumentNames', 'schemas']


class DocumentNames(Enum):
    start = 'start'


SCHEMA_PATH = 'schemas'
SCHEMA_NAMES = {DocumentNames.start: 'schemas/run_start.json'}
schemas = {}
for name, filename in SCHEMA_NAMES.items():
    with open(rs_fn(SCHEMA_PATH, filename)) as fin:
        schemas[name] = json.load(fin)
