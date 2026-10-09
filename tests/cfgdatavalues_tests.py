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

    def test_get_toml(self):
        cfg_data = CfgDataValues()
        cfg_data.set_value('max_slide_width', 1600)
        cfg_data.set_value('max_slide_height', 1200)

        expected_toml = "max_slide_width = 1600\nmax_slide_height = 1200\n"
        self.assertEqual(cfg_data.get_toml(), expected_toml)

    def test_get_toml_empty(self):
        cfg_data = CfgDataValues()
        expected_toml = ""
        self.assertEqual(cfg_data.get_toml(), expected_toml)