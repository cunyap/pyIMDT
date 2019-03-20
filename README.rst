pyIMD
-----
The aim of this module is the calculation of the total/inertial mass for measurements taken in the continous sweep or in the phase-lock loop (PLL) mode.

Installation
------------

To install this module, type on a cmd shell::

    >>> git clone https://git.bsse.ethz.ch/cunya/pyIMD
    >>> cd pyIMD
    >>> pip install .

Usage
-----

To use this module, write::

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

Note
----

Use tab completion to access the object's attributes (e.g. to get the calculated mass)::

    >>> mass = obj.calculated_cell_mass

Known Issues
------------

In a IPython notebook the progress bar works not properly but has no effect on the calculations.
In a IPython notebook the calculation speed is much slower.