from setuptools import setup, find_packages

setup(
    name='unigen',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'mutagen>=1.47.0'
    ]
)