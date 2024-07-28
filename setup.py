from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='unigen',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'mutagen>=1.47.0'
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)