from os.path import dirname, join
from setuptools import setup
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

with open(join(dirname(__file__), 'ulib/VERSION.txt'), 'rb') as f:
    VERSION = f.read().decode('utf8').strip()

with open(join(dirname(__file__), 'README.md'), 'rb') as f:
    LONG_DESCRIPTION = f.read().decode('utf8').strip()

setup(
    name='ulib',
    version=VERSION,
    description='talib wrapper for intellisense',
    long_description=LONG_DESCRIPTION,
    author='ueqt',
    author_email='ueqtxu@gmail.com',
    url='https://github.com/ueqt/talib',
    license='MIT',
    packages=['ulib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[str(ir.req) for ir in parse_requirements(
        'requirements.txt', session=False
    )],
    entry_points={
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Cython',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
    ]
)
