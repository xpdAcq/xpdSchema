import json
from pkg_resources import resource_filename as rs_fn

if __name__ == '__main__':
    schema = rs_fn('xpdschema', 'schemas/run_start.json')
    with open(schema) as f:
        json.load(f)
