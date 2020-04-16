import wx

class SMGFrame(wx.Frame):    
	def __init__(self):
		super().__init__(parent=None, title='Star Map Generator')
		mainPanel = wx.Panel(self)

		self.xSize = wx.TextCtrl(mainPanel,pos=(5,5))
		generateBtn = wx.Button(mainPanel, label="Generate Map",pos=(5,55))

		self.Show()
