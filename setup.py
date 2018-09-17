import os
from setuptools import setup

setup(
    name='pyaskpass',
    version='0.0.1',
    description='Pure Python Askpass',
    author='Matt Kubilus',
    author_email='mattkubilus@gmail.com',
    url='https://github.com/kubilus1/pyaskpass',
    install_requires=[
        'pyglet'
    ],
    scripts=['askpass']
)
