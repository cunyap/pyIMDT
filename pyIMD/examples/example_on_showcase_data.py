from pyIMD.imd import InertialMassDetermination

# Create the inertial mass determination object
imd = InertialMassDetermination()

# Create a config file for the project / experiment to analyze using default values. Note non default parameters can be
# added as optional arguments for e.g. spring_constant = 5.
file_path1 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Showcase data\\Showcase data\\mass data\\20190110_ShowCase_PLL_B.txt"
file_path2 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Showcase data\\Showcase data\\mass data\\20190110_ShowCase_PLL_A.txt"
file_path3 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Showcase data\\Showcase data\\mass data\\20190110_ShowCase_PLL_LongTerm.txt"
imd.create_pyimd_project(file_path1, file_path2, file_path3, '\t', 23, 'PLL', figure_width=5.4, figure_height=9.35,
                         figure_unit='cm',
                         initial_parameter_guess=[73.0, 5.2, 0.0, 0.0], upper_parameter_bounds=[90.0, 7, 3.0, 3.0],
                         spring_constant=8, cell_position=9.5, figure_format='pdf',
                         correct_for_frequency_offset=False, frequency_offset_n_measurements_used=15)

# Print the config file to the console to check if all parameters are set correctly before starting the calculation.
imd.print_pyimd_project()
# If one needs to change a parameter on the fly just type: imd.settings.<parameter_key> = value as eg.
# imd.settings.figure_resolution_dpi = 300. Note: Just hit imd.settings. + TAB to get automatically a list of all
# available <parameter_keys>
# imd.show_settings_dialog()

# Run the inertial mass determination
imd.run_inertial_mass_determination()

# Save the config file for the project / experiment for documentation purpose or to re-run with different /
# same parameter later
#imd.load_pyimd_project()
#imd.save_pyimd_project("C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Showcase data\\Showcase data\\mass data\\pyIMDShowCaseProject2.xml")