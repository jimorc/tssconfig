import toml
import unittest
from src.cfg_data_values import CfgDataValues

class TestCfgDataValues(unittest.TestCase):
    def test_set_default_values(self):
        cfg_data = CfgDataValues()
        cfg_data.set_default_values()
        
        self.assertEqual(cfg_data.get_value('max_slide_width'), 1400)
        self.assertEqual(cfg_data.get_value('max_slide_height'), 1050)

    def test_get_value_nonexistent_key(self):
        cfg_data = CfgDataValues()
        cfg_data.set_default_values()
        
        self.assertIsNone(cfg_data.get_value('nonexistent_key'))

    def test_set_and_get_value(self):
        cfg_data = CfgDataValues()
        cfg_data.set_default_values()
        
        cfg_data.set_value('max_slide_width', 1600)
        cfg_data.set_value('max_slide_height', 1200)
        
        self.assertEqual(cfg_data.get_value('max_slide_width'), 1600)
        self.assertEqual(cfg_data.get_value('max_slide_height'), 1200)

    def test_dumps(self):
        cfg_data = CfgDataValues()
        cfg_data.set_value('max_slide_width', 1600)
        cfg_data.set_value('max_slide_height', 1200)

        expected_toml = "max_slide_width = 1600\nmax_slide_height = 1200\n"
        self.assertEqual(cfg_data.dumps(), expected_toml)

    def test_dumps_empty(self):
        cfg_data = CfgDataValues()
        expected_toml = ""
        self.assertEqual(cfg_data.dumps(), expected_toml)

    def test_loads_valid_toml(self):
        cfg_data = CfgDataValues()
        toml_string = "max_slide_width = 1600\nmax_slide_height = 1200\n"
        cfg_data.loads(toml_string)

        self.assertEqual(cfg_data.get_value('max_slide_width'), 1600)
        self.assertEqual(cfg_data.get_value('max_slide_height'), 1200)

    def test_loads_invalid_toml(self):
        cfg_data = CfgDataValues()
        invalid_toml_string = "max_slide_width = 1600\nmax_slide_height\n"
        
        with self.assertRaises(toml.TomlDecodeError):
            cfg_data.loads(invalid_toml_string)

    def test_loads_non_string(self):
        cfg_data = CfgDataValues()
        non_string_input = 12345
        
        with self.assertRaises(TypeError):
            cfg_data.loads(non_string_input)