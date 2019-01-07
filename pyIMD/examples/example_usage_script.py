from pyIMD.inertialmassdetermination import InertialMassDetermination

# Create the inertial mass determination object
imd = InertialMassDetermination()
# Create a config file for the project / experiment to analyze
imd.create_config()
# Print the config file (optionally imd.validate_config can be run to check if it is complete)
imd.print_config()
# Run the inertial mass determination
imd.obj.run_intertial_mass_determination()
# Save the config file for the project / experiment
imd.save_config()