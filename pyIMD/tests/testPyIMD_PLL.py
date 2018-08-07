from pyIMD.inertialmassdetermination import InertialMassDetermination

file_path1 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20170712_RSN_3_B"
file_path2 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20170712_RSN_3_A"
file_path3 = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20170712_RSN_3_A_long_term.tdms"
obj = InertialMassDetermination(file_path1, file_path2, file_path3, '\t', 23, 1)
# print(obj.settings)
obj.run_intertial_mass_determination()
type(obj.data_measured)
#
# from nptdms import TdmsFile, TdmsWriter
#
# tdms_file = TdmsFile(file_path3)
# df = tdms_file.as_dataframe(time_index=False, absolute_time=False)
# print('done')
# with TdmsWriter("copied_file.tdms") as copied_file:
#     copied_file.write_segment(obj.data_measured)

# from nptdms import TdmsFile
# tdms_file = TdmsFile(file_path3)
# g = tdms_file.groups()
# print(g)
# print(tdms_file.group_channels('Parameters'))
# print(tdms_file.group_channels('Data'))
#
# channel = tdms_file.object('Group', 'Data')
# data = channel.data
# # do stuff with data
#
# from nptdms import TdmsWriter, ChannelObject
# import numpy
#
# with TdmsWriter("path_to_file.tdms") as tdms_writer:
#     data_array = numpy.linspace(0, 1, 10)
#     channel = ChannelObject('Group', 'Channel1', data_array)
#     tdms_writer.write_segment([channel])
#
