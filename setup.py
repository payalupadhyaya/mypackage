from setuptools import setup, find_packages

setup(
    name='MyFirstPackage',
    version='0.1dev',
    packages=find_packages(),
#    packages=['mypack',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)


