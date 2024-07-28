from setuptools import setup, find_packages

with open("README.md", "f") as f:
    description = f.read()

setup(
    name='unigen',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'mutagen>=1.47.0',
        'pydantic>=2.8.2'
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)