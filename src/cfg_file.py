import os
from pathlib import Path

class CfgFile:
    """
    A class to handle the reading and writing of the configuration file.
    """
    def __init__(self, path: Path = None):
        """
        Initializes the CfgFile instance.

        Args:
            path (Path, optional): The path to the configuration file. If not provided, the default path is set to ~/.config/tssconfig.toml.
        """
        self.path = path if path is not None else CfgFile.get_config_file_path()

    @staticmethod
    def get_config_file_path() -> Path:
        """
        Returns:
            Path: The path to the default configuration file.
        """
        return Path.home() / ".config" / "tssconfig.toml"

    def get_path(self) -> Path:
        """
        Returns the path to the configuration file.

        Returns:
            Path: The path to the configuration file.
        """
        return self.path

    def write(self, data: str):
        """
        Writes the provided data to the configuration file.

        Args:
            data (str): The data to write to the configuration file.

        Raises:
            IOError: If there is an error writing to the file.
        """
        with open(self.path, 'w') as f:
            f.write(data)

    def read(self) -> str:
        """
        Reads the data from the configuration file.

        Returns:
            str: The data read from the configuration file.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            IOError: If there is an error reading the file.
        """
        with open(self.path, 'r') as f:
            return f.read()