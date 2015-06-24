from setuptools import setup
import shutil
setup(name='usefulholidays',
      version='0.1',
      description='The disrupting package to check the school calendar :) ',
      url='https://github.com/WRPLA/usefulholidays',
      author='brios',
      license='T4T-Rios',
      packages=['usefulholidays'],
      package_data={'usefulholidays': ['*.db']},
      zip_safe=False)