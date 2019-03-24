Welcome to pyIMD!
=================================

.. image:: https://img.shields.io/badge/Made%20with-Python-brightgreen.svg
        :target: https://www.python.org/
        :alt: made-with-python
  
.. image:: https://img.shields.io/pypi/pyversions/pyimd.svg
        :target: https://www.python.org/
        :alt: made-with-python3.6
  
.. image:: https://img.shields.io/badge/platform-linux--x64%20%7C%20osx--x64%20%7C%20win--64-lightgrey.svg
        :alt: supported-platform      

.. image:: https://img.shields.io/badge/license-GPLv3-brightgreen.svg
        :target: https://git.bsse.ethz.ch/cunya/pyimd/master/LICENSE
        :alt: License

.. image:: https://readthedocs.org/projects/pyimd/badge/?version=latest
        :target: https://pyimd.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
        
.. raw:: html
    <img src="/pyIMD/examples/figures/pyIMD_ShowCaseFigure-01.png" height="100px">

.. figure:: pyIMD/examples/figures/pyIMD_ShowCaseFigure_web.png
    :width: 400 px
    :alt: result

    Evolution of mass over time and the corresponding microscopy images are shown for a time span of 20min.
    The mass data was acquired every 10ms (data shown in black), overlaid in red is the rolling mean with a window of
    1000. Images taken every 3 min over the observed times span, we see on average a steady increase of the cell mass.

With the introduction of a picoscopic cell balance that is compatible with optical microscopy, a new tool for the
investigation of the cell state-dependent cell mass regulation is available for use in biophysics, cell biology,
physiology and medicine. However, the analysis of the data can be challenging due to a) the amount of high resolution
data or b) the structure of low-stress measurement (low resolution) data. Here, we introduce the software **pyIMD**, which
allows to easily extract the mass as a function of time for non-moving cells out of the raw data. **pyIMD** Stands for
Python inertial mass determination.


This documentation of **pyIMD** describes the API as well as gives provides a sample data set as well as sample scripts to
run **pyIMD** from Jupyter or the Python console but it also contains a tutorial about how pyIMD is used with the user
interface.
The aim of this module is the calculation of the total/inertial mass for measurements taken in the continuous sweep or in the phase-lock loop (PLL) mode.

Links
=====

* `Documentation <https://pyimd.readthedocs.io>`_
* `PyPI <https://pypi.org/project/pyimd>`_

Installation
------------
If you download the portable for your operating system there is no need for any installation and you can use **pyIMD**
directly trough the user interface.

To install this module from source, type on your terminal::

    >>> git clone https://git.bsse.ethz.ch/cunya/pyIMD
    >>> cd pyIMD
    >>> pip install .

Usage
-----

To use this module in a Python script, write::

    >>> from pyIMD.inertialmassdetermination import InertialMassDetermination

    >>> file_path1 = "Path/to/measurement_no_cell"
    >>> file_path2 = "Path/to/measurement_with_cell"
    >>> file_path3 = "Path/to/measurement.tdms"
    >>> obj = InertialMassDetermination(file_path1, file_path2, file_path3, '\t', 23, 0)
    >>> obj.run_intertial_mass_determination()


List default settings for calculation::

    >>> obj.settings.__dict__

Change settings for calculation and figure output the following way before calling run_intertial_mass_determination()::

    >>> obj.settings.SPRING_CONSTANT = 4

More info and examples can be found in the online `Documentation <https://pyimd.readthedocs.io>`_

Note
----

Use tab completion to access the object's attributes (e.g. to get the calculated mass)::

    >>> mass = obj.calculated_cell_mass

Known Issues
------------

In a IPython notebook the progress bar works not properly but has no effect on the calculations.
In a IPython notebook the calculation speed is much slower.