import wx
import wx.lib.intctrl

from wx.lib.masked import NumCtrl

from makeMap import *
from SMGMapPanel import SMGMapPanel


class SMGFrame(wx.Frame):    
	def __init__(self):
		super().__init__(parent=None, title='Star Map Generator')
		self.Center()
		mainPanel = wx.Panel(self)

		#Sizer for entire window
		self.mainSizer = wx.BoxSizer()
		#sizer for left half of window
		inputSizer = wx.BoxSizer(wx.VERTICAL)
		#sizer for the input data parameters		
		dataSizer = wx.StaticBoxSizer(wx.VERTICAL,mainPanel,label = "Map Parameters")

		#x dimension
		sizer1 = wx.BoxSizer(wx.HORIZONTAL)
		xSizeLabel = wx.StaticText(mainPanel,label="Map Width (x):")
		sizer1.Add(xSizeLabel,0,wx.TOP,10)
		self.xSize = wx.lib.intctrl.IntCtrl(mainPanel,min=1)
		sizer1.Add(self.xSize,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer1,0,wx.ALIGN_RIGHT)

		#y dimension
		sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		ySizeLabel = wx.StaticText(mainPanel,label="Map Height (y):")
		sizer2.Add(ySizeLabel,0,wx.TOP,10)
		self.ySize = wx.lib.intctrl.IntCtrl(mainPanel,min=1)
		sizer2.Add(self.ySize,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer2,0,wx.ALIGN_RIGHT)

		#z dimension
		sizer3 = wx.BoxSizer(wx.HORIZONTAL)
		zSizeLabel = wx.StaticText(mainPanel,label="Map Thickness (z):")
		sizer3.Add(zSizeLabel,0,wx.TOP,10)
		self.zSize = wx.lib.intctrl.IntCtrl(mainPanel,min=1)
		sizer3.Add(self.zSize,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer3,0,wx.ALIGN_RIGHT )

		#stellar density
		sizer4 = wx.BoxSizer(wx.HORIZONTAL)
		densityLabel = wx.StaticText(mainPanel,label="Stellar Density:")
		sizer4.Add(densityLabel,0,wx.TOP,10)
		self.stellarDensity = NumCtrl(mainPanel,min=0,fractionWidth=4)
		sizer4.Add(self.stellarDensity,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer4,0,wx.ALIGN_RIGHT )

		#text scale
		sizer5 = wx.BoxSizer(wx.HORIZONTAL)
		textScaleLabel = wx.StaticText(mainPanel,label="Text Scale:")
		sizer5.Add(textScaleLabel,0,wx.TOP,10)
		self.textScale = NumCtrl(mainPanel,min=0.25,fractionWidth=2)
		sizer5.Add(self.textScale,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer5,0,wx.ALIGN_RIGHT )

		#output map filename
		sizer6 = wx.BoxSizer(wx.HORIZONTAL)
		outMapNameLabel = wx.StaticText(mainPanel,label="Output Map Filename:")
		sizer6.Add(outMapNameLabel,0,wx.TOP,10)
		self.outMapName = wx.TextCtrl(mainPanel)
		sizer6.Add(self.outMapName,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer6,0,wx.ALIGN_RIGHT )

		#output data filename
		sizer7 = wx.BoxSizer(wx.HORIZONTAL)
		outDataNameLabel = wx.StaticText(mainPanel,label="Output Data Filename:")
		sizer7.Add(outDataNameLabel,0,wx.TOP,10)
		self.outDataName = wx.TextCtrl(mainPanel)
		sizer7.Add(self.outDataName,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer7,0,wx.ALIGN_RIGHT )

		#input data filename
		sizer8 = wx.BoxSizer(wx.HORIZONTAL)
		inDataNameLabel = wx.StaticText(mainPanel,label="Input Data Filename:")
		sizer8.Add(inDataNameLabel,0,wx.TOP,10)
		self.inDataName = wx.TextCtrl(mainPanel)
		sizer8.Add(self.inDataName,0,wx.ALL|wx.EXPAND,5)
		dataSizer.Add(sizer8,0,wx.ALIGN_RIGHT )

		#print z coordinate
		sizer9 = wx.BoxSizer(wx.HORIZONTAL)
		printZLabel = wx.StaticText(mainPanel,label="Print Z coordinate:")
		sizer9.Add(printZLabel,0,wx.TOP,5)
		self.printZ = wx.CheckBox(mainPanel)
		sizer9.Add(self.printZ,0,wx.ALL,5)
		dataSizer.Add(sizer9,0,wx.ALIGN_RIGHT )


		inputSizer.Add(dataSizer,0)
		
		#buttons
		btnSizer = wx.BoxSizer()
		generateBtn = wx.Button(mainPanel, label="Generate Map")
		generateBtn.Bind(wx.EVT_BUTTON, self.generateMap)
		btnSizer.Add(generateBtn,0,wx.ALL,5)
		clearBtn = wx.Button(mainPanel, label = "Reset Values")
		clearBtn.Bind(wx.EVT_BUTTON,self.resetParameters)
		btnSizer.Add(clearBtn,0,wx.ALL,5)

		inputSizer.Add(btnSizer,0,wx.ALL|wx.CENTER,5)

		self.mainSizer.Add(inputSizer,0,wx.ALL,5)

		#map display area
		mapSizer = wx.StaticBoxSizer(wx.VERTICAL,mainPanel,label = "Map")
		mapSizer = wx.FlexGridSizer(1,1,wx.Size(0,0))
		mapSizer.AddGrowableCol(0)
		mapSizer.AddGrowableRow(0)
		mapSizer.SetFlexibleDirection(wx.BOTH)

		self.mapPanel = SMGMapPanel(mainPanel);
		mapSizer.Add(self.mapPanel,1,wx.ALL|wx.EXPAND,5)

		self.mainSizer.Add(mapSizer,1,wx.ALL|wx.EXPAND,5)

		#set defaults for the inputs
		self.setDefaults()

		# finalize display
		self.mainSizer.SetSizeHints(self)
		mainPanel.SetSizer(self.mainSizer)
		mainPanel.Layout()

		self.Bind(wx.EVT_SIZE,self.onResize)

		self.Show()


	def generateMap(self,event):
		# set up parameters
		p = self.createParamDict()
		# create the map
		self.createMap(p)
		# display the map
		self.drawMap(p['filename'])

	def resetParameters(self,event):
		self.setDefaults()

	def setDefaults(self):
		self.xSize.SetValue(20)
		self.ySize.SetValue(20)
		self.zSize.SetValue(20)
		self.stellarDensity.SetValue(0.004)
		self.textScale.SetValue(1)
		self.outMapName.SetValue('sampleMap.svg')
		self.outDataName.SetValue('sampleMap.dat')
		self.inDataName.SetValue('')
		self.printZ.SetValue(True)

	def createParamDict(self):
		p={}
		p['maxX'] = self.xSize.GetValue()
		p['maxY'] = self.ySize.GetValue()
		zVal = self.zSize.GetValue()//2
		p['minZ'] = -zVal
		p['maxZ'] = zVal
		if (0==(self.zSize.GetValue()%2)): #for even values
			p['minZ'] = p['minZ']+1
		p['stellarDensity'] = self.stellarDensity.GetValue()
		p['filename'] = self.outMapName.GetValue()
		p['datafile'] = self.outDataName.GetValue()
		p['scale'] = self.textScale.GetValue()
		p['printZ'] = self.printZ.GetValue()

		return p

	def createMap(self,p):
		loadFile = "YaziraSectorData.txt"
		if (self.inDataName.GetValue() != ""): # read the data from the specified file
			from loadData import loadData
			starList=[]
			jumpList = []
			loadData(self.inDataName.GetValue(),p,starList,jumpList)
		else:  # generate the data randomly
			starList = createSystems(p)
			jumpList = findJumps(starList)

		print ("there are",len(starList),"systems on the map")

		# check for overlapping systems and flag
		multipleList = findOverlaps(starList)
	
		defDict = {} # dictionary of gradient definitions for star symbols in SVG file
		# generate symbols for each system
		symbolList = createMapSymbols(p,starList,multipleList,defDict)
	
		# generate stellar distance data
		connectionList = findConnections(starList,jumpList)
	
		# draw map
		createMap(p,defDict,symbolList,connectionList,starList)
	
		#write out the star system data
		from writeData import writeSystemData,writeConnectionData
		writeSystemData(p,starList)
		writeConnectionData(p,jumpList)

		#make a PNG as well
		#cairosvg.svg2png(url=p["filename"], write_to=p["filename"]+".png")


	def drawMap(self,file):
		self.mapPanel.setMap(file)
		self.mainSizer.Layout()
		self.Update()
		self.Refresh()

	def onResize(self,event):
		self.Update()
		self.Refresh()
		wx.Event.Skip(event)
