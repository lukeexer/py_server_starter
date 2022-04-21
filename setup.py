from setuptools import setup

setup(
   name='sserver',
   version='1.0',
   description='Simple server starter.',
   author='Luke',
   packages=['slib', 'server'],
   install_requires=[
       'flask',
       'redis']
)