pyIMD
-----

To install this module, simply do on a cmd shell::

    >>> git clone https://git.bsse.ethz.ch/cunya/pyIMD
    >>> cd pyIMD
    >>> pip install .

To use this module, simply do::

    >>> from pyIMD.inertialmassdetermination import InertialMassDetermination
    >>> file_path1 = "Path/to/measurement_no_cell"
    >>> file_path2 = "Path/to/measurement_with_cell"
    >>> file_path3 = "Path/to/measurement.tdms"
    >>> obj = InertialMassDetermination(file_path1, file_path2, file_path3, '\t', 23, 0)
    >>> obj.run_intertial_mass_determination()

Use tab completion to access the object's attributes (eg. to get the calculated mass)
    >>> mass = obj.calculated_cell_mass

