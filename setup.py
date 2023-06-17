from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="sweatDB",
    version='2.0.1',
    author="0xsweat",
    author_email="<0x.sweat@tutanota.com>",
    description='A python3 DBMS',
    long_description_content_type="text/markdown",
    long_description='A database management system with an easier syntax than SQL',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'python database management system', 'DBMS'],
    classifiers=[]
)
