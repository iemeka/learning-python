try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
    name='djangotut',
    version='0.0.1',
    description='learning django',
    license='mit',
    packages=['djangotut'],
    scripts =[''],
    author='emeka',
    author_email='mekstines@gmail.com',
    keywords=[''],
    url='heynowbrowncow'
)