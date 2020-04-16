import wx

class SMGFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Star Map Generator')
        self.Show()
