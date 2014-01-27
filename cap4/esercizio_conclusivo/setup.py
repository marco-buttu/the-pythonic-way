from distutils.core import setup

setup(
    name = 'pyfinder',
    version = '1.0',
    description  = 'Utilities to find files and file contents',
    long_description = open('README').read(),
    py_modules = ['pyfinder'],
    author = 'Marco Buttu',
    author_email = "marco.buttu@gmail.com",
    license = 'GPL',
    url = 'https://pypi.python.org/pypi/pyfinder/',
    keywords = 'python generators distutils',
    scripts = ['scripts/pyfinder'],
    platforms = 'all',
    classifiers = [
        'Intended Audience :: Students, Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Text Processing :: Filters',
        'Topic :: Files'
   ],
)

