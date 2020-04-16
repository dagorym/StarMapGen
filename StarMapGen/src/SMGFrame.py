import wx

class SMGFrame(wx.Frame):    
	def __init__(self):
		super().__init__(parent=None, title='Star Map Generator')
		mainPanel = wx.Panel(self)

		inputSizer = wx.BoxSizer(wx.VERTICAL)
		self.xSize = wx.TextCtrl(mainPanel)
		inputSizer.Add(self.xSize,0,wx.ALL|wx.EXPAND,5)
		generateBtn = wx.Button(mainPanel, label="Generate Map")
		generateBtn.Bind(wx.EVT_BUTTON, self.generateMap)
		inputSizer.Add(generateBtn,0,wx.ALL|wx.CENTER,5)
		mainPanel.SetSizer(inputSizer)

		self.Show()

	def generateMap(self,event):
		value = self.xSize.GetValue()
		if not value:
			print("You didn't enter anything")
		else:
			print(f'You typed: "{value}"')
