from pyIMD.imd import InertialMassDetermination

# Create the inertial mass determination object
imd = InertialMassDetermination()

# Create a config file for the project / experiment to analyze using default values. Note non default parameters can be
# added as optional arguments for e.g. spring_constant = 5.
file_path1 = "C:\\<PATH>\\ExampleData\\20170712_RSN_3_B"
file_path2 = "C:\\<PATH>\\ExampleData\\20170712_RSN_3_A"
file_path3 = "C:\\<PATH>\\ExampleData\\20170712_RSN_3_A_long_term.tdms"
imd.create_pyimd_project(file_path1, file_path2, file_path3, '\t', 23, 'PLL')

# Print the config file to the console to check if all parameters are set correctly before starting the calculation.
imd.print_pyimd_project()

# If one needs to change a parameter on the fly just type: imd.settings.<parameter_key> = value as eg.
# imd.settings.figure_resolution_dpi = 300

# Run the inertial mass determination
imd.run_intertial_mass_determination()

# Save the config file for the project / experiment for documentation purpose or to re-run with different /
# same parameter later
imd.save_pyimd_project("C:\\<PATH>\\ExampleData\\pyIMDProjectName.xml")
