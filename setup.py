from setuptools import setup


def extract_version():
    """Return pyIMD.__version__ from pyIMD/__init__.py
    """
    with open('pyIMD/__init__.py') as fd:
        ns = {}
        for line in fd:
            if line.startswith('__version__'):
                exec(line.strip(), ns)
                return ns['__version__']


setup(name='pyIMD',
      version=extract_version(),
      author='Andreas P. Cuny <andreas.cuny@bsse.ethz.ch>, Gotthold Flaeschner <gotthold.flaeschler@bsse.ethz.ch>',
      author_email="andreas.cuny@bsse.ethz.ch",
      url='https://git.bsse.ethz.ch/cunya/pyIMD',
      download_url='https://git.bsse.ethz.ch/cunya/pyIMD',
      description='Inertial mass determination',
      long_description='',
      packages={'pyIMD': 'pyIMD',
                'pyIMD.analysis': 'pyIMD/analysis',
                'pyIMD.error': 'pyIMD/error',
                'pyIMD.tests': 'pyIMD/tests',
                'pyIMD.io': 'pyIMD/io',
                'pyIMD.plotting': 'pyIMD/plotting',
                'pyIMD.ui': 'pyIMD/ui',
                'pyIMD.configuration': 'pyIMD/configuration'},
      package_dir={'pyIMD': 'pyIMD',
                   'pyIMD.analysis': 'pyIMD/analysis',
                   'pyIMD.tests': 'pyIMD/tests',
                   'pyIMD.io': 'pyIMD/io',
                   'pyIMD.plotting': 'pyIMD/plotting',
                   'pyIMD.ui': 'pyIMD/ui',
                   'pyIMD.configuration': 'pyIMD/configuration'},
      keywords='Inertial mass determination',
      license='GPL2.0',
      classifiers=['Development Status :: 1 - Alpha',
                   'Intended Audience :: Developers, Users',
                   'Natural Language :: English',
                   'Operating System :: Linux :: Linux',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Topic :: Scientific/Engineering'
                   ],
      install_requires=['pandas==0.23.3', 'numpy==1.14.5', 'scipy==1.1.0', 'nptdms==0.12.0', 'tqdm==4.23.4',
                        'plotnine==0.3.0', 'PyQT5', 'lxml', 'xmltodict', 'matplotlib'],

      )
