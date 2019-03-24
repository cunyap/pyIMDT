from pyIMD.imd import InertialMassDetermination
from pyIMD.ui.resource_path import resource_path

# Create the inertial mass determination object
imd = InertialMassDetermination()

# Create a config file for the project / experiment to analyze using default values. Note non default parameters can be
# added as optional arguments for e.g. spring_constant = 5.
#file_path1 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\IMD_Data_Yeast_Measurements\\PLL\\20180601\\20190110_ShowCase_PLL_B.txt"
#file_path2 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\IMD_Data_Yeast_Measurements\\PLL\\20180601\\20190110_ShowCase_PLL_A.txt"
#file_path3 = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Showcase data\\Showcase data\\mass data\\20190110_ShowCase_PLL_LongTerm.txt"
#imd.create_pyimd_project(file_path1, file_path2, file_path3, '\t', 23, 'PLL', figure_width=16.5, figure_height=20,
#                         initial_parameter_guess=[73.0, 5.2, 0.0, 0.0], upper_parameter_bounds=[90.0, 7, 3.0, 3.0],
#                         spring_constant=8, cell_position=9.5, figure_format='pdf')

# Print the config file to the console to check if all parameters are set correctly before starting the calculation.
imd.print_pyimd_project()
print(resource_path('SuperConfig.xml'))
imd.save_pyimd_project(resource_path('SuperConfig.xml'))

with open('SuperConfig.xml', 'r') as myfile:
  data = myfile.read()

print(data)