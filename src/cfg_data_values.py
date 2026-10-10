import toml

class CfgDataValues:
    """
    A class to hold the config data values for the slideshow.

    This class contains default values for various settings related to a 
    slideshow, such as the maximum slide width and height, text for the start
    and end slides, sort order, and so forth.
    
    Objects of this class can be used to provide program-wide defaults, and
    also to provide default values for individual slideshows. The class can be
    extended to include additional settings as needed.
    """
    def __init__(self):
        """
        Creates an empty CfgDataValues instance.
        
        Actual initialiation of the values is done in other methods, such as
        `set_default_values()`.
        """
        self.data = {}

    def set_default_values(self):
        """
        Sets the default values for the configuration data.
        """
        self.data = {}
        # width and height are in pixels
        self.data['max_slide_width'] = 1400
        self.data['max_slide_height'] = 1050

    def get_value(self, key):
        """
        Gets the value for a given key from the configuration data.

        Args:
            key (str): The key for which to retrieve the value.
        """
        return self.data.get(key, None)

    def set_value(self, key, value):
        """
        Sets the value for a given key in the configuration data.

        Args:
            key (str): The key for which to set the value.
            value: The value to set for the given key.
        """
        self.data[key] = value

    def dumps(self):
        """
        Returns the configuration data as a string in TOML format.

        Returns:
            str: The configuration data in TOML format.
        """
        return toml.dumps(self.data)

    def loads(self, toml_string):
        """
        Sets the configuration data from a string in TOML format.

        Args:
            toml_string (str): The TOML string to parse and set as configuration data.
        
        Raises:
            toml.TomlDecodeError: If the provided string is not valid TOML.
            TypeError: If the provided string is not a string type.
        """
        self.data = toml.loads(toml_string)
