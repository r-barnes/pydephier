[![DOI](https://zenodo.org/badge/179896888.svg)](https://zenodo.org/badge/latestdoi/179896888)


pydephier: Depression Hierarchies for Python
======================

Prerequisites
-------------

Although GDAL is not required to use the library, it is needed to run the
example program.

Install the prerequisites

### Linux

    sudo apt install libgdal-dev cmake

### Mac

    brew install gdal libomp cmake

Compilation
-----------

Run
```bash
python3 setup.py install --user
```

To run tests you can use:
```bash
pip3 install nose
nosetests -v .
```

Citation
--------

 * Computing water flow through complex landscapes, Part 2: Finding hierarchies in depressions and morphological segmentations (doi: [10.5194/esurf-2019-34](https://doi.org/10.5194/esurf-2019-34))