import os
from pathlib import Path

class CfgFile:
    """
    A class to handle the reading and writing of the configuration file.
    """
    @staticmethod
    def get_path() -> Path:
        """
        Returns:
            Path: The path to the configuration file.
        """
        return Path.home() / ".config" / "tssconfig.toml"
