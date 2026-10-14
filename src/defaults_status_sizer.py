"""
Display status messages as program attempts to load
the tssconfig default values from the tssconfig.toml file.
"""
import wx

from src.cfg_file import CfgFile
from src.cfg_data_values import CfgDataValues

class DefaultsStatusSizer(wx.BoxSizer):
    """
    Panel used to display the status messages
    """
    BORDER = 10

    def __init__(self, parent: wx.Frame):
        super(DefaultsStatusSizer, self).__init__()
        self.parent = parent
        self.data = CfgDataValues()
        f = CfgFile()
        status = f.load_defaults(self.data)

        text = wx.StaticText(parent, label = status)
        text.SetForegroundColour(wx.BLUE)
        pnl_sizer = wx.BoxSizer(wx.VERTICAL)
        pnl_sizer.Add(wx.StaticLine(parent,
                                    size=wx.Size(
                                        parent.GetClientSize().GetWidth(), -1)))
        pnl_sizer.Add(text, 50, flag=wx.ALL, border=self.BORDER)
        pnl_sizer.Add(wx.StaticLine(parent,
                                    size=wx.Size(
                                        parent.GetClientSize().GetWidth(), 1)),
                                    proportion=1,
                                    flag=wx.BOTTOM)
        button_sizer = self.create_button_bar_sizer()
        pnl_sizer.Add(button_sizer, 1, flag=wx.RIGHT)

        self.Add(pnl_sizer, 1)

    def create_button_bar_sizer(self) -> wx.BoxSizer:
        sizer = wx.BoxSizer()

        edit = wx.Button(self.parent, label="Edit Defaults")
        edit.SetToolTip("Click to edit default values")
        edit.Bind(wx.EVT_BUTTON, self.parent.onEditDefaults)

        quit = wx.Button(self.parent, label="Quit")
        quit.SetToolTip("Click to terminate the program")
        quit.Bind(wx.EVT_BUTTON, self.parent.OnExit)

        config = wx.Button(self.parent, label="Configure Slideshow")
        config.SetToolTip("Click to configure the slideshow")
        config.Bind(wx.EVT_BUTTON, self.parent.onConfigSlideshow)

        sizer.AddSpacer(200)
        sizer.Add(edit, flag=wx.ALL, border=10)
        sizer.Add(config, flag=wx.ALL, border=10)
        sizer.Add(quit, flag=wx.ALL, border=10)
        return sizer