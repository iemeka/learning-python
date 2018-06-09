try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
    name='iread',
    version='0.0.1',
    description='read your text just the way you like it!',
    license='MIT',
    packages=['readtxt'],
    scripts =["bin/readit"],
    author='emeka',
    author_email='mekstines@gmail.com',
    keywords=[],
    url=''
)

