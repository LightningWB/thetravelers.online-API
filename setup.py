from setuptools import setup

setup(name='thetravelers.online Api',
      version='1.1.0',
      description='Python API for thetravelers.online',
      long_description='An API for thetravelers.online written in python using a headless firefox. You need firefox installed first.',
      author='LightningWB',
      url='https://github.com/LightningWB/thetravelers.online-API',
      packages=['travelersApi'],
      install_requires=['selenium']
     )