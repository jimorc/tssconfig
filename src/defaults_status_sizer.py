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
        button_sizer.Realize()
        pnl_sizer.Add(button_sizer, 1, flag=wx.RIGHT)

        self.Add(pnl_sizer, 1)

    def create_button_bar_sizer(self) -> wx.StdDialogButtonSizer:
        sizer = wx.StdDialogButtonSizer()

        edit = wx.Button(self.parent, label="Edit Defaults",
                         id=wx.ID_CANCEL)
        edit.SetToolTip("Click to edit default values")
        edit.Bind(wx.EVT_BUTTON, self.parent.onEditDefaults)

        sizer.Add(edit,flag=wx.ALL, border = 5)
        return sizer