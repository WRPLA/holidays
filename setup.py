from setuptools import setup
from pip.req import parse_requirements
import shutil

install_reqs = parse_requirements('usefulholidays/requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]
setup(install_requires = reqs,
      name='usefulholidays',
      version='0.1',
      description='The disrupting package to check the school calendar :) ',
      url='https://github.com/WRPLA/usefulholidays',
      author='brios',
      license='T4T-Rios',
      packages=['usefulholidays'],
      package_data={'usefulholidays': ['*.db']},
      zip_safe=False)