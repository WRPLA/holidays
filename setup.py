from setuptools import setup
import shutil
setup(name='usefulholidays',
      version='0.1',
      description='The disrupting package to check the school calendar :) ',
      url='https://github.com/WRPLA/usefulholidays',
      author='brios',
      license='T4T-Rios',
      packages=['usefulholidays'],
      zip_safe=False)
print('lol')
shutil.move('/usr/local/lib/python3.4/site-packages/usefulholidays-0.1-py3.4.egg/usefulholidays',
          '/usr/local/Cellar/python3/3.4.3/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages')