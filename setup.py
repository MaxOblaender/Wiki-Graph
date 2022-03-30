
from setuptools import setup
setup(
    name = 'Wiki-Graph',
    version = '0.1.0',
    packages = ['wikigraph'],
    entry_points = {
        'console_scripts': [
            'wikigraph = wikigraph.__main__:main'
        ]
    })