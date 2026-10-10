import os
from pathlib import Path
import shutil
import unittest

from src.cfg_file import CfgFile
from src.cfg_data_values import CfgDataValues

class TestCFGFile(unittest.TestCase):
    def test_get_config_file_path(self):
        # Test that get_path returns the expected value
        self.assertEqual(CfgFile.get_config_file_path(), 
                         Path.home() / ".config" / "tssconfig" / "tssconfig.toml")

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

    def test_bad_write(self):
        # Test that writing to a file in a non-existent directory raises an 
        # OSError
        cfg_file = CfgFile(path=Path("/non_existent_directory/config.toml"))
        with self.assertRaises(OSError):
            cfg_file.write("test_data")

    def test_bad_write_permission(self):
        # Test that writing to a file without write permissions raises an 
        # OSError
        cfg_file = CfgFile(path=
                           Path("test/test/no_write_permission_config.toml"))
        if os.path.exists("test/"):
            os.chmod("test/", 0o755)
            shutil.rmtree("test/")
        os.makedirs("test", 0o644)
        try:
            cfg_file.write("new_test_data")
        except PermissionError:
            pass
        except OSError as io:
            self.fail("Should have thrown PermissionError not OSError")
        finally:
            shutil.rmtree("test/")  # Clean up the test file

    def test_bad_read_permission(self):
        # Test that reading from a file without read permissions raises an 
        # OSError
        cfg_file = CfgFile(path=Path("no_read_permission_config.toml"))
        with open(cfg_file.get_path(), 'w') as f:
            f.write("test_data")
        os.chmod(cfg_file.get_path(), 0o000)  # Remove read permissions
        with self.assertRaises(OSError):
            cfg_file.read()
        os.chmod(cfg_file.get_path(), 0o644)  # Restore permissions
        os.remove(cfg_file.get_path())  # Clean up the test file

    # Calls to CfgFile.load_defaults has side effects. Because of this, it is
    # necessary to force sequential execution of all tests on that method.
    # Therefore, all tests must be placed in this test method.
    def test_load_defaults(self):
        # test config file doesn't exist
        # delete config file
        f = CfgFile()
        if f.exists():
            f.remove()
        data = CfgDataValues()
        status = CfgFile.load_defaults(data)
        self.assertIn("Configuration file does not exist. ", status,
                        "Config file does not exist test failed.")
        self.assertIn("Will attempt to save default values.", status,
                      "Will attempt - config file does not exist test failed.")
        self.assertTrue(f.exists())
        self.assertIn("Defaults file written.", status)

        # PermissionsError on defaults file write
        f.remove()
        os.chmod(f.parent(), 0x444)
        status = CfgFile.load_defaults(data)
        os.chmod(f.parent(), 0o755)
        self.assertIn("Configuration file does not exist. ", status,
                      "Config file does not exist - permissions test failed.")
        self.assertIn("Will attempt to save default values.", status,
                      "Will attempt - permissions test failed.")
        self.assertIn("Defaults file could not be saved.", status,
                      "Config file - permissions failed.")

        # I cannot determine how to generate an OSError
