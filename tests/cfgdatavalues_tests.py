import unittest
from src.cfg_data_values import CfgDataValues

class TestCfgDataValues(unittest.TestCase):
    def test_set_default_values(self):
        cfg_data = CfgDataValues()
        cfg_data.set_default_values()
        
        self.assertEqual(cfg_data.max_slide_width, 1400)
        self.assertEqual(cfg_data.max_slide_height, 1050)