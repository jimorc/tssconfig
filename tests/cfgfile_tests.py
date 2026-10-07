import os
from pathlib import Path
import unittest

from src.cfg_file import CfgFile

class TestCFGFile(unittest.TestCase):
    def test_get_config_file_path(self):
        # Test that get_path returns the expected value
        self.assertEqual(CfgFile.get_config_file_path(), 
                         Path.home() / ".config" / "tssconfig.toml")

    def test_init_with_custom_path(self):
        # Test that the CfgFile can be initialized with a custom path
        custom_path = Path("config.toml")
        cfg_file = CfgFile(path=custom_path)
        self.assertEqual(cfg_file.get_path(), custom_path)

    def test_init_with_default_path(self):
        # Test that the CfgFile initializes with the default path when no path
        # is provided
        cfg_file = CfgFile()
        self.assertEqual(cfg_file.get_path(), CfgFile.get_config_file_path())

    def test_write_and_read_config_file(self):
        # Test writing to and reading from the configuration file
        cfg_file = CfgFile()
        test_data = "test_key = 'test_value'"
        
        # Write test data to the config file
        cfg_file.write(test_data)

        # Read the data back from the config file
        read_data = cfg_file.read()
        os.remove(cfg_file.get_path())  # Clean up the test file
        
        self.assertEqual(read_data, test_data)

    def test_bad_read(self):
        # Test that reading from a non-existent file raises a FileNotFoundError
        cfg_file = CfgFile(path=Path("non_existent_config.toml"))
        with self.assertRaises(FileNotFoundError):
            cfg_file.read()
