from setuptools import setup
import shutil

with open('usefulholidays/requirements.txt') as f:
    required = f.read().splitlines()
setup(install_requires = required,
      name='usefulholidays',
      version='0.1',
      description='The disrupting package to check the school calendar :) ',
      url='https://github.com/WRPLA/usefulholidays',
      author='brios',
      license='T4T-Rios',
      packages=['usefulholidays'],
      package_data={'usefulholidays': ['*.db']},
      zip_safe=False)