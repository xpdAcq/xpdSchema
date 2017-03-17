import json
from pkg_resources import resource_filename as rs_fn


__all__ = ['DocumentNames', 'schemas']


SCHEMA_PATH = 'xpdschema'
SCHEMA_NAMES = {'start': 'schemas/run_start.json'}
schemas = {}
for name, filename in SCHEMA_NAMES.items():
    with open(rs_fn(SCHEMA_PATH, filename)) as fin:
        schemas[name] = json.load(fin)
