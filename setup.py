from distutils.core import setup
from setuptools import find_packages
setup(
   name='math_quiz',
   version='0.1',
   author="HuberJakob",
   author_email="jakob.huber@fau.de",
   packages=find_packages(),
   long_description=open('README.txt').read(),
   install_requires=["random"],
)