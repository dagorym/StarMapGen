import wx
import wx.svg
import wx.lib.wxcairo
import cairocffi

class SMGMapPanel(wx.Panel):
	"""A panel to hold and display the generated map"""

	def __init__(self,parent):
		super(SMGMapPanel,self).__init__(parent)
		
		self.mapFile = "test.svg"
		self.img = wx.svg.SVGimage.CreateFromFile(self.mapFile)
		self.SetMinSize(wx.Size(400,400))

		#hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		#st1 = wx.StaticText(self, label='Some Text')
		#hbox1.Add(st1,0,wx.ALL|wx.EXPAND,5)
		self.Bind(wx.EVT_PAINT,self.onPaint)

	def onPaint(self, event):
		dc = wx.PaintDC(self)
		dc.SetBackground(wx.Brush('black'))
		dc.Clear()

		dcdim = min(self.Size.width, self.Size.height)
		imgdim = min(self.img.width, self.img.height)
#		print (self.Size.width,self.Size.height)
#		print (self.img.width,self.img.height)
		scale = dcdim / imgdim
#		print (scale)
		width = int(self.img.width * scale)
		height = int(self.img.height * scale)
#		print(width,height)
		
		gr = wx.GraphicsRenderer.GetCairoRenderer()
		ctx = gr.CreateContext(dc)
		self.img.RenderToGC(ctx, scale)
	
	def setMap(self,file):
		self.img = wx.svg.SVGimage.CreateFromFile(file)
		self.Refresh()