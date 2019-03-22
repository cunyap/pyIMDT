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

The total mass of single cells can be accurately monitored in real time under physiological conditions with our recently
developed picobalance. It is a powerful tool to investigate crucial processes in biophysics, cell biology or medicine,
such as cell mass regulation. However, processing of the raw data can be challenging, as computation is needed to extract
the mass and long-term measurements can generate large amounts of data. Here, we introduce the software package **pyIMD**  that
automates raw data processing, particularly when investigating non-migrating cells. **pyIMD** Stands for
Python inertial mass determination and is implemented using Python 3.6 and can be used as a command line tool
or as a stand-alone version including a graphical user interface. 


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

