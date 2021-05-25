from setuptools import find_packages, setup

VERSION = "0.1.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="locky",
    version=VERSION,
    description="locky - simple action verification mechanism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moonburnt/locky",
    author="moonburnt",
    author_email="moonburnt@disroot.org",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    packages=find_packages(),
    install_requires=[],
    )
