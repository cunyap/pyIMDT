from setuptools import setup

setup(name='pyIMD',
      version='0.0.1',
      author='Andreas P. Cuny <andreas.cuny@bsse.ethz.ch>, Gotthold Fl�schner <gotthold.flaeschler@bsse.ethz.ch>',
      url='https://git.bsse.ethz.ch/cunya/pyIMD',
      download_url='https://git.bsse.ethz.ch/cunya/pyIMD',
      description='Inertial mass determination',
      long_description='',
      packages={'pyIMD': 'pyIMD',
                'pyIMD.analysis': 'pyIMD/analysis',
                'pyIMD.error': 'pyIMD/error',
                'pyIMD.tests': 'pyIMD/tests',
                'pyIMD.file_io': 'pyIMD/file_io',
                'pyIMD.visualization': 'pyIMD/visualization'},
      package_dir={'pyIMD': 'pyIMD',
                   'pyIMD.analysis': 'pyIMD/analysis',
                   'pyIMD.tests': 'pyIMD/tests',
                   'pyIMD.file_io': 'pyIMD/file_io',
                   'pyIMD.visualization': 'pyIMD/visualization'},
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
      install_requires=['pandas==0.23.3', 'numpy==1.14.5', 'scipy==1.1.0', 'nptdms==0.12.0', 'tqdm==4.23.4', 'ggplot'],
      dependency_links=['git+https://git@github.com/cunyap/ggpy.git#egg+ggplot-0.11.5']
      )
