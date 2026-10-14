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
        self.data = CfgDataValues()
        f = CfgFile()
        status = f.load_defaults(self.data)

        text = wx.StaticText(parent, label = status)
        text.SetForegroundColour(wx.BLUE)
        pnl_sizer = wx.BoxSizer(wx.VERTICAL)
        pnl_sizer.Add(wx.StaticLine(parent,
                                    size=wx.Size(
                                        parent.GetClientSize().GetWidth(), -1)))
        pnl_sizer.Add(text, 1, flag=wx.ALL, border=self.BORDER)

        self.Add(pnl_sizer, 1)
