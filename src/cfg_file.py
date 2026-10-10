import os
from pathlib import Path
from src.cfg_data_values import CfgDataValues

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
        return Path.home() / ".config" / "tssconfig" / "tssconfig.toml"

    def get_path(self) -> Path:
        """
        Returns the path to the configuration file.

        Returns:
            Path: The path to the configurationpass file.
        """
        return self.path

    def write(self, data: str):
        """
        Writes the provided data to the configuration file.

        Args:
            data (str): The data to write to the configuration file.

        Raises:
            PermissionError: If the directory does not exist and cannot be
                created, or if user does not have write permission on parent
                directories.
            OSError: If there is an error writing to the file.
        """
        if not self.path.parent.exists():
            os.makedirs(self.path.parent, mode=0o755, exist_ok=True)
        with open(self.path, 'w') as f:
            f.write(data)

    def read(self) -> str:
        """
        Reads the data from the configuration file.

        Returns:
            str: The data read from the configuration file.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            OSError: If there is an error reading the file.
        """
        with open(self.path, 'r') as f:
            return f.read()

    def exists(self) -> bool:
        """
        Determines if the file exists.

        Returns True if file exists, False otherwise
        """
        return self.get_path().exists()

    def remove(self):
        """
        Deletes file if it exists.
        """
        os.remove(self.get_path())

    def parent(self) -> Path:
        '''
        Retrieve parent directory of this file.

        Returns:
            Path to parent directory of this file.
        '''
        try:
            parent = self.path.parent
            return parent
        except Exception as e:
            print(e)

    @staticmethod
    def load_defaults(data: CfgDataValues) -> str:
        """
        Load contents of defaults file into data argument.

        Args:
            data (CfgDataValues): configuration data either returned from
                config file or default values if config file does not exist,
                or if an error occured while trying to retrieve file contents.

        Returns:
            str specifying status information related to load attempt.
        """
        status = ""
        f = CfgFile()
        if f.exists():
            pass
        else:
            status = "Configuration file does not exist. "
            status += "Will attempt to save default values.\n"
            data.set_default_values()
            toml = data.dumps()
            try:
                f.write(toml)
                status += "Defaults file written.\n"
            except PermissionError:
                status += "Defaults file could not be saved. "
                status += "User does not have permission to write defaults "
                status += "file.\n"
            except IOError as io:
                status += format("IO error: {io} encountered while trying ")
                status += "to write defaults file\n"
        return status

