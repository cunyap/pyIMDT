.. pyIMD documentation master file, created by
   sphinx-quickstart on Mon Jan  7 11:51:05 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyIMD's documentation!
=================================

.. image:: https://img.shields.io/badge/Made%20with-Python-brightgreen.svg
        :target: https://www.python.org/
        :alt: made-with-python


.. figure:: ../examples/figures/pyIMD_ShowCaseFigure-01.png
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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   group
   api
   authors
   license
   references


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

