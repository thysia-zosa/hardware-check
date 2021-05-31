from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='hardwareCheck',
   version='1.0',
   description='A useful hardware monitoring tool',
   long_description=long_description,
   author='Jonas Tochterman, Melvin Tas, Severin Hasler',
   author_email='jonas.tochterman@edu.tbz.ch',
   packages=['hardware-check'],  #internal packages | same as name
   install_requires=['crontab', 'PyYAML', 'pyspectator', 'requests'], #external packages as dependencies
)