from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='hardwareCheck',
   version='1.0',
   description='A useful hardware monitoring tool',
   long_description=long_description,
   author='Jonas Tochtermann, Melvin Tas, Severin Hasler',
   author_email='jonas.tochtermann@edu.tbz.ch',
   packages=['hardware-check'],  #internal packages | same as name
   install_requires=['python-crontab', 'pyyaml', 'pyspectator', 'requests'], #external packages as dependencies
)