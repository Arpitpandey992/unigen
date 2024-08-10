from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

packages = find_packages()
packages.remove("unigen.tests")  # remove tests to avoid bloating the package

setup(
    name="unigen",
    version="1.4.2.post2",
    packages=packages,
    install_requires=[
        "mutagen",
    ],
    tests_require=[
        "pytest",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
