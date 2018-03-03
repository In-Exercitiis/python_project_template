'''All the meta data about a project that is used for
setup.py. __about__.py based on a talk given by Hyak Wuffelkaker or
something like that. Can't remember his name, can't find him online.

'''

__all__ = [
    '__author__', '__classifiers__', '__desc__', '__license__',
    '__package_name__', '__scripts__', '__url__', '__version__',
]

__author__ = 'Luke Powers'
__author_email__ = 'luke-powers@users.noreply.github.com'
# For more classifiers, see http://goo.gl/zZQaZ
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
    'Private :: Do Not Upload'
    # Do not allow this package to be uploaded to pypi.python.org
]
__desc__ \
    = '''Template project meant for quickly generating installable python packages.'''
__entry_points__ = {
    'console_scripts':
    [
        'some_console_script=template_project.__main__:script_fn',
    ]
}
__license__ = 'Apache Software License 2.0'
__package_exclude__ = ['tests']
__package_name__ = 'template_project'
__requires__ = [
    'pip>=9.0'
    ]
__scripts__ = []
__url__ = 'http://github.com/%s/%s' % (__author__.replace(' ', '-'), __package_name__)
__version__ = '0.0.1'
