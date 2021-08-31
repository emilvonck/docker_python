import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))


# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


setup(
    name="docker_python",
    version="1.0",
    description="A simple python module",
    author="emilvonck",
    author_email="emilvonck@test.local",
    py_modules=["docker_python"],
    entry_points={"console_scripts": ["docker_python=docker_python:main"]},
)