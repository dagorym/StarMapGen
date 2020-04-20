import wx
import wx.svg
import wx.lib.wxcairo
import cairocffi

class SMGMapPanel(wx.Panel):
	"""A panel to hold and display the generated map"""

	def __init__(self,parent,w=20,h=20):
		super(SMGMapPanel,self).__init__(parent)
		
		self.mapFile = "BannerMap.svg"
		self.img = wx.svg.SVGimage.CreateFromFile(self.mapFile)
		ratio=w/h
		self.SetMinSize(wx.Size(400*ratio,400))

		self.Bind(wx.EVT_PAINT,self.onPaint)

	def onPaint(self, event):
		dc = wx.PaintDC(self)
		dc.SetBackground(wx.Brush('black'))
		dc.Clear()

		self.computeScale()
		
		gr = wx.GraphicsRenderer.GetCairoRenderer()
		ctx = gr.CreateContext(dc)
		self.img.RenderToGC(ctx, self.scale)
#		self.Update()
	
	def setMap(self,file):
		self.img = wx.svg.SVGimage.CreateFromFile(file)
		self.computeScale()

	def computeScale(self):
		scale1 = self.Size.width/self.img.width
		scale2 = self.Size.height/self.img.height
		self.scale = min(scale1,scale2)
		width = int(self.img.width * self.scale)
		height = int(self.img.height * self.scale)
		print (self.scale, width,height)
		self.SetSize(wx.Size(width,height))
