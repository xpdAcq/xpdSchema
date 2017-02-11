from setuptools import setup

setup(name='xpdschema',
      packages=['xpdschema'],
      version='0.0.0-alpha',
      package_data={'xpdschema': ['schemas/*.json']},
      include_package_data=True)
