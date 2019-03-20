pyIMD User Interface Tutorial
=============================

Before starting, make sure pyIMD is :doc:`installed </installation>`

This tutorial provides a simple example with a test dataset, teaching step by step how to:

    - create a pyIMD project
    - calculate the mass form the measured data

First, lets have a look at the input data. The typical data set consists of 3 files. Two sweep files of the cantilever
without and with a cell attached to it as text files with a multi-line header and the actual (long-term) measurement file.
Either as text file or as TDMS file. A typical time resolution is 10 ms for the data acquisition so these files can be
quite large. **Fig. 1** visualizes the data input which can be found as example data set for download and testing.

.. figure:: ../examples/figures/pyIMD_ShowCase_InputData.png
    :alt: dataInput

    **Figure 1**: Data format for pyIMD

The Example pyIMD script section demonstrated how a pyIMD project is created on the console:

.. code-block:: python

    from pyIMD.imd import InertialMassDetermination

    # Create the inertial mass determination object
    imd = InertialMassDetermination()

    # Create a config file for the project / experiment to analyze using default values. Note non default parameters can be
    # added as optional arguments for e.g. spring_constant = 5.
    file_path1 = "C:\\Users\\<USERNAME>\\PyIMD Showcase data\\0190110_ShowCase_PLL_B.txt"
    file_path2 = "C:\\Users\\<USERNAME>\\PyIMD Showcase data\\20190110_ShowCase_PLL_A.txt"
    file_path3 = "C:\\Users\\<USERNAME>\\PyIMD Showcase data\\20190110_ShowCase_PLL_LongTerm.txt"
    imd.create_pyimd_project(file_path1, file_path2, file_path3, '\t', 23, 'PLL', figure_width=16.5, figure_height=20,
                             initial_parameter_guess=[60.0, 2.0, 0.0, 0.0], cell_position=9.5, figure_format='pdf')

In the stand alone mode using pyIMD trough its user interface (UI), the pyIMD project is created in exact the same way
in the background. The user does not need to take care to type the paths or arguments correctly as all the input entered
trough the UI will be validated automatically. **Fig. 2** shows the main window and the settings window of the pyIMD program.
A new pyIMD project is simply created by selecting from a directory using (3) at least three data files required for the
calculation as described in **Fig. 1**. Next, the relationship of the selected files to which measurement they correspond
needs to be determined, the measurement mode set in (5). Using the menu (1) or hitting Ctrl+P the settings dialog opens
and lets you determine all the required and optional parameters such as the names of the output figures. After all settings
are set the mass calculation is started with (6).

.. code-block:: python

    # Run the inertial mass determination
    imd.run_inertial_mass_determination()

The console (8) logs all actions performed with the UI and indicates when all calculations are done. The results can be
viewed in the results tab (2) where as all the output figures are listed as well as the data can be inspected.

.. figure:: ../examples/figures/pyIMD_UI_Figure.png
    :alt: uiExample

    **Figure 2**: pyIMD user interface: (1) Trough the menu bar a pyIMD project can be loaded, saved and the settings and parameter
    dialog can be opened (shown at the right hand side). The help menu contains the software documentation, the quick
    help (also shown during startup), change log and information about the software authors. (2) With the tabs
    the single or batch calculation mode can be selected. After all  calculations are done the
    result tab is enabled and shows the latest result such as figures and resulting data in tabular form in (7).
    (3) Creates a new pyIMD project while selecting at least three data files required for the calculation. (4) The
    relationship of the selected files to which measurement they correspond needs to be determined here. (5) Sets the
    measurement mode the data was acquired with. (6) Starts the mass calculation. (2: Batch processing) One or multiple
    pyIMD project files can be selected which will then be run sequentially in different threads. With the settings dialog
    on the right all the required parameters needed for the calculation are set as well as specifications of e.g. the output
    file formats or file names. The input is validated live and if a parameter of a wrong type is entered, the input field
    turns yellow notifying the user to correct the mistake.

The first output created by pyIMD are control figures visualizing the fit of the cantilevers phase response is shown for
the case with and without cell (**Fig. 3**). The shift towards lower frequencies can be clearly seen, when the cell is attached.
Moreover, the Q-factor changes and therefore the slope of the response curve. If the fits are not fitting the raw data
the parameter 'initial_parameter_guess', 'lower_parameter_bounds', 'upper_parameter_bounds' need to be adjusted in the
settings dialog (Note: hit Ctrl + P to show the settings dialog.)

.. figure:: ../examples/figures/PreStartFrequencyShift.png
    :alt: preStartFreqFit

    **Figure 3**: Frequency vs cantilever phase response

The analysis is shown as outputted by the software in **Fig. 4**, the exemplary data for a mammalian cell is provided for download.
The evolution of mass vs time is shown for a time span of 20min. The mass data was acquired every 10ms (data shown in
black), overlaid in red is the rolling mean with a window of 1000 (adjustable parameter 'rolling_window_size'). Images
taken every 3 min  over the observed time span, we see on average a steady increase of the cell mass, the spring constant
is 8N/m (adjustable parameter 'sprint_constant'). The position of the cell projected along the long axis of the
cantilever was 9.5um (adjustable parameter, 'cell_position') and did not change, which is of importance for
the current use of the software.

.. figure:: ../examples/figures/pyIMD_ShowCaseFigure-01.png
    :alt: result

    **Figure 4**: Evolution of mass over time

The project can either be re-run with different parameters to i.e. improve the function fits or be saved using the menu
(**Fig. 2**, (1)).

.. code-block:: python

    # save a pyIMD project
    imd.save_pyimd_project("C:\\Users\\<USERNAME>\\PyIMD Showcase data\\pyIMDShowCaseProject.xml")

A previously saved project can be loaded again at a later time from the menu (**Fig. 2**, (1))or also from the command
line without the user interface:

.. code-block:: python

    # load a pyIMD project
    imd.load_pyimd_project("C:\\Users\\<USERNAME>\\PyIMD Showcase data\\pyIMDShowCaseProject.xml")

