from pyIMD.inertialmassdetermination import InertialMassDetermination

file_path1 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20170712_RSN_3_B"
file_path2 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20170712_RSN_3_A"
file_path3 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20180703_SBC_3_C_2_A_long_term.tdms"
obj = InertialMassDetermination(file_path1, file_path2, file_path3, '\t', 23, 0)
obj.run_intertial_mass_determination()
