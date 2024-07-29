from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="unigen",
    version="1.2",
    packages=find_packages(),
    install_requires=["mutagen", "pydantic"],
    tests_require=[
        "pytest",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
