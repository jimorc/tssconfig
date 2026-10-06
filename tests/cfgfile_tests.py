from pathlib import Path
import unittest
from src.cfg_file import CfgFile

class TestCFGFile(unittest.TestCase):
    def test_get_path(self):
        # Test that get_path returns the expected value
        self.assertEqual(CfgFile.get_path(), 
                         Path.home() / ".config" / "tssconfig.toml")



if __name__ == '__main__':
    unittest.main()