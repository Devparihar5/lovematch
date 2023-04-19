from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.6.0'
DESCRIPTION = 'Love Match Calculator'
LONG_DESCRIPTION = 'A Python package to calculate love match percentage between two names.'

# Setting up
setup(
    name="lovematch",
    version=VERSION,
    author="Devendra Parihar",
    author_email="devendraparihar340@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'love', 'match', 'percentage', 'calculator', 'lovematch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)