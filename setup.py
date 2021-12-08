import setuptools
# from setuptools.command.build_ext import build_ext as _build_ext
import re
import subprocess
from typing import List


# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension

richdem_compile_time = None
richdem_git_hash     = None

if richdem_git_hash is None:
  try:
    shash = subprocess.Popen(["git log --pretty=format:'%h' -n 1"], shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.readlines()[0].decode('utf8').strip()
    sdate = subprocess.Popen(["git log -1 --pretty='%ci'"], shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout.readlines()[0].decode('utf8').strip()
    if re.match(r'^[0-9a-z]+$', shash) and re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.*$', sdate):
      richdem_compile_time = sdate
      richdem_git_hash     = shash
  except:
    print("Warning! Could not find RichDEM version. Software will still work, but reproducibility will be compromised.")
    pass

if richdem_git_hash is None:
  richdem_compile_time = 'Unknown'
  richdem_git_hash     = 'Unknown'

print("Using RichDEM hash={0}, time={1}".format(richdem_git_hash, richdem_compile_time))

ext_modules: List[Pybind11Extension] = [
  Pybind11Extension("pydephier",
    [
      'submodules/Barnes2019-DepressionHierarchy/submodules/richdem/src/gdal.cpp',
      'submodules/Barnes2019-DepressionHierarchy/submodules/richdem/src/random.cpp',
      'submodules/Barnes2019-DepressionHierarchy/submodules/richdem/src/richdem.cpp',
      'src/pydephier.cpp'
    ],
    include_dirs  = [
      'submodules/Barnes2019-DepressionHierarchy/include/',
      'submodules/Barnes2019-DepressionHierarchy/submodules/richdem/include',
    ],
    define_macros = [
      ('DOCTEST_CONFIG_DISABLE', None                ),
      ('RICHDEM_COMPILE_TIME',   f'"\\"{richdem_compile_time}\\""'),
      ('RICHDEM_GIT_HASH',       f'"\\"{richdem_git_hash}\\""'    ),
      ('RICHDEM_LOGGING',        None                ),
      ('_USE_MATH_DEFINES',      None) #To ensure that `#include <cmath>` imports `M_PI` in MSVC
    ],
    extra_compile_args = [
      '-std=c++17',
      '-Wno-unknown-pragmas'
    ]
  )
]

#TODO: https://packaging.python.org/tutorials/distributing-packages/#configuring-your-project
setuptools.setup(
  name             = 'pydephier',
  version          = '0.0.1',
  description      = 'Depression Hierarchies for Python',
  url              = 'https://github.com/r-barnes/pydephier',
  author           = 'Richard Barnes',
  author_email     = 'rijard.barnes@gmail.com',
  license          = 'GPLv3',
  packages         = setuptools.find_packages(),
  ext_modules      = ext_modules,
  keywords         = 'TODO',
  install_requires = [
    "numpy>=1.7,<2; python_version > '3.4' or python_version < '3.0'",
    "numpy>=1.7,<1.12; python_version < '3.4' and python_version > '3.0'"
  ],

  #TODO: https://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers      = [
      'Development Status :: 4 - Beta',

      'Environment :: Console',

      'Intended Audience :: Developers',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'Intended Audience :: Other Audience',

      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

      'Natural Language :: English',

      'Topic :: Scientific/Engineering :: GIS',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Visualization',
      'Topic :: Software Development :: Libraries',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.8',
  ]
)
