from xmlunittest import XmlTestCase
from pyIMD.imd import InertialMassDetermination
from pyIMD.ui.resource_path import resource_path


class CustomTestCase(XmlTestCase):

    def test_my_custom_test(self):
        # Create the inertial mass determination object
        imd = InertialMassDetermination()
        # Save the project
        imd.save_pyimd_project(resource_path('TestConfig.xml'))

        with open('TestConfig.xml', 'rb',) as myfile:
            data = myfile.read()

        print(data)

        # Everything starts with `assertXmlDocument`
        root = self.assertXmlDocument(data)

        # Check
        self.assertXmlNode(root, tag='PyIMDSettings')
        self.assertXpathValues(root, './GeneralSettings/figure_format/text()', 'png')
        self.assertXpathValues(root, './GeneralSettings/figure_width/text()', '56.44')
        self.assertXpathValues(root, './GeneralSettings/figure_height/text()', '45.16')
        self.assertXpathValues(root, './GeneralSettings/figure_units/text()', 'cm')
        self.assertXpathValues(root, './GeneralSettings/figure_resolution_dpi/text()', '72')
        self.assertXpathValues(root, './GeneralSettings/figure_name_pre_start_no_cell/text()', 'FitNoCellData')
        self.assertXpathValues(root, './GeneralSettings/figure_name_pre_start_with_cell/text()', 'FitWithCellData')
        self.assertXpathValues(root, './GeneralSettings/figure_name_measured_data/text()', 'CalculatedCellMass')
        self.assertXpathValues(root, './GeneralSettings/figure_plot_every_nth_point/text()', '1')
        self.assertXpathValues(root, './GeneralSettings/conversion_factor_hz_to_khz/text()', '1000.0')
        self.assertXpathValues(root, './GeneralSettings/conversion_factor_deg_to_rad/text()', '-57.3')
        self.assertXpathValues(root, './GeneralSettings/spring_constant/text()', '4.0')
        self.assertXpathValues(root, './GeneralSettings/cantilever_length/text()', '100')
        self.assertXpathValues(root, './GeneralSettings/cell_position/text()', '9.5')
        self.assertXpathValues(root, './GeneralSettings/initial_parameter_guess/text()', '[70.0, 2.0, 0.0, 0.0]')
        self.assertXpathValues(root, './GeneralSettings/lower_parameter_bounds/text()', '[10.0, 1.0, -3, -3]')
        self.assertXpathValues(root, './GeneralSettings/upper_parameter_bounds/text()', '[100.0, 5.0, 3, 3]')
        self.assertXpathValues(root, './GeneralSettings/rolling_window_size/text()', '1000')
        self.assertXpathValues(root, './GeneralSettings/frequency_offset/text()', '0')
        self.assertXpathValues(root, './GeneralSettings/read_text_data_from_line/text()', '23')
        self.assertXpathValues(root, './GeneralSettings/text_data_delimiter/text()', '\t')
        self.assertXpathValues(root, './ProjectSettings/selected_files/File/text()',
                               ('20190110_ShowCase_PLL_A.txt', '20190110_ShowCase_PLL_B.txt',
                                '20190110_ShowCase_PLL_LongTerm.txt'))
        self.assertXpathValues(root, './ProjectSettings/project_folder_path/text()', '')
        self.assertXpathValues(root, './ProjectSettings/pre_start_no_cell_path/text()', '')
        self.assertXpathValues(root, './ProjectSettings/pre_start_with_cell_path/text()', '')
        self.assertXpathValues(root, './ProjectSettings/measurements_path/text()', '')
        self.assertXpathValues(root, './ProjectSettings/calculation_mode/text()', 'PLL')

        self.assertXpathsUniqueValue(root, ('./leaf/@id',))
        self.assertXpathValues(root, './leaf/@active', ('on', 'off'))
