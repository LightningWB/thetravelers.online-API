from setuptools import setup

file = open('./README.md', 'r')
readme = file.read()
file.close()

setup(name='thetravelers.online Api',
	version='1.3.0',
	description='Python API for thetravelers.online',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='LightningWB',
	url='https://github.com/LightningWB/thetravelers.online-API',
	packages=['travelersApi'],
	install_requires=['selenium'],
	license='MIT'
)