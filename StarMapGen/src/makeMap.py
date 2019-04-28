#!/usr/bin/env python
from random import randint,seed
from StarSystem import StarSystem
from math import sqrt,atan,acos,copysign,sin,cos,fabs

def createDef(spType,starData,dDict):
	"""Create the gradient definitions for the star symbols
	
	Each star symbol consists of three components that each is
	a unique color and gradient.  The colors are based on the
	spectral type of the star but the gradients are the same
	regardless of spectral type.  This function creates the gradient
	information and returns the gradient names to be used.
	
	To help minimize the size of the resultant SVG file, gradients
	are only generated for the spectral types that will be on the
	map.  The gradients are stored in a dictionary, indexed by
	an ID based on the spectral type of the star.  This dictionary
	is passed in as one of the parameters and if the requested
	gradient is already there, the function simply returns the list
	of gradients to use for the specified star.
	
	Inputs:
	 - spType - The spectral type of the star
	 - starData - A list containing information about the size of
	              the star symbol and the colors to be used
	 - dDict - the definition dictionary that will hold the
	           definition information
	           
	Outputs:
	 - gList - a list of the three gradients needed for the
	           specified star.
	"""
	g1 = "rg" + spType + "a"
	g2 = "rg" + spType + "b"
	g3 = "rg" + spType + "c"

	gList = [g1,g2,g3]	
	
	if g1 not in dDict:
#		print ("Adding " + g1 + " definition")
		r1 = 100 * starData[0]
		s1 = '  <radialGradient id="%s" gradientUnits="userSpaceOnUse" r="%f">\n' % (g1,r1)
		s1 += '   <stop stop-color="%s" offset="0"/>\n' % (starData[1][0])
		s1 += '   <stop stop-color="%s" stop-opacity="0" offset="1"/>\n'% (starData[1][0])
		s1 += '  </radialGradient>\n'
		dDict[g1]=s1

	if g2 not in dDict: 
#		print ("Adding " + g2 + " definition")
		r2 = 56.25 * starData[0]
		s2 = '  <radialGradient id="%s" gradientUnits="userSpaceOnUse" r="%f">\n' % (g2,r2)
		s2 += '   <stop stop-color="%s" offset="0"/>\n' % (starData[1][1])
		s2 += '   <stop stop-color="%s" offset="0.54545"/>\n' % (starData[1][1])
		s2 += '   <stop stop-color="%s" stop-opacity="0" offset="1"/>\n'% (starData[1][1])
		s2 += '  </radialGradient>\n'
		dDict[g2]=s2

	if g3 not in dDict:
#		print ("Adding " + g3 + " definition")
		r3 = 50 * starData[0]
		s3 = '  <radialGradient id="%s" gradientUnits="userSpaceOnUse" r="%f">\n' % (g3,r3)
		s3 += '   <stop stop-color="%s" offset="0"/>\n' % (starData[1][2])
		s3 += '   <stop stop-color="%s" stop-opacity=".86432" offset="0.5"/>\n' % (starData[1][2])
		s3 += '   <stop stop-color="%s" stop-opacity="0" offset="1"/>\n'% (starData[1][2])
		s3 += '  </radialGradient>\n'
		dDict[g3]=s3

	return gList

def createSymbol(spType,pos,dDict):
	starData = getParams(spType)
	gList = createDef(spType,starData,dDict)
	s = ' <g transform="translate(%f,%f)">\n' %tuple([starData[0]*i for i in pos])
	if ("NS" == spType or "BH" == spType):
		s += '  <path style="fill:#ffffff;" d="m -4,-40 a 6.35,54.2 0 0 1 7,-7.5 l -2.8,48.5 z" transform="matrix(-0.8,0.6,-0.6,-0.8,0,0)" />'
	s += '  <circle r="%f" fill="black"/>\n' % (starData[0]*55.)
	s += '  <circle r="%f" fill="url(#%s)"/>\n' % (starData[0]*100.,gList[0])
	s += '  <circle r="%f" fill="url(#%s)"/>\n' % (starData[0]*75.,gList[1])
	s += '  <circle r="%f" fill="url(#%s)"/>\n' % (starData[0]*50.,gList[2])
	if ("NS" == spType or "BH" == spType):
			s += '  <path style="fill:#ffffff;" d="m -4,-40 a 6.35,54.2 0 0 1 7,-7.5 l -2.8,48.5 z" transform="matrix(0.8,-0.6,0.6,0.8,0,0)" />'
	s += ' </g>\n'
	return s

def getParams(spType):
	return {
		'O0': [0.75,["#5579ff","#1345ff","#9cb2ff"]],  #TODO currently using B0 colors, get unique
		'B0': [0.75,["#5579ff","#1345ff","#9cb2ff"]],
		'A0': [0.5,["#688bff","#2256ff","#b9c9ff"]],
		'F0III': [0.75,["#9cb2ff","#607aff","#e0e4ff"]],
		'G0III': [0.75,["#fffcb6","#fffa72","#fff8fc"]],
		'K0III': [0.75,["#ffc58d","#ff9228","#ffeedd"]],
		'M0III': [0.75,["#ff9f41","#ff7e00","#ffc38b"]],
		'F0I': [1,["#9cb2ff","#607aff","#e0e4ff"]],
		'G0I': [1,["#fffcb6","#fffa72","#fff8fc"]],
		'K0I': [1,["#ffc58d","#ff9228","#ffeedd"]],
		'M0I': [1,["#ff9f41","#ff7e00","#ffc38b"]],
		'F0': [0.5,["#9cb2ff","#607aff","#e0e4ff"]],
		'G0': [0.5,["#fffcb6","#fffa72","#fff8fc"]],
		'K0': [0.5,["#ffc58d","#ff9228","#ffeedd"]],
		'M0': [0.25,["#ff9f41","#ff7e00","#ffc38b"]],
		'BD': [0.20,["#ff26b0","#ff4000","#ff64c8"]],
		'WD': [0.25,["#5579ff","#1345ff","#9cb2ff"]],
		'NS': [0.375,["#c86400","#804000","#ff8000"]], 
		'BH': [0.375,["#0000ff","#ff0000","#000000"]], 
	}.get(spType,[0.25,["rgM0a","rgM0b","rgM0c"]]);
	
def sortSpecTypeForDisplay(st):
	rank = {
		#supergiants
        'F0I': 30,
        'G0I': 40,
        'K0I': 50,
        'M0I': 60,
        #giants
        'F0III': 130,
        'G0III': 140,
        'K0III': 150,
        'M0III': 160,
        #main sequence
        'O0': 110,
        'B0': 120,
        'A0': 220,
        'F0': 230,
        'G0': 240,
        'K0': 250,
        'M0': 500,
        #brown dwarfs
        'BD': 2000,
        #collapsars
        'WD': 1000,
        'NS': 400,
        'BH': 410,    
    }
	return rank[st]
	
def writeDefs(f,dDict):
	f.write(" <defs>\n")
	for x in dDict:
		f.write(dDict[x])
	f.write(" </defs>\n")

def writeSymbols(f,sList):
	for x in sList:
		f.write(x)
		
def createSystems(p):
	"""Create all the star systems
	
	This function first generates the number of systems based on the
	map dimensions and the specified stellar density
	
	After the number of systems are determined, a list of StarSystem
	objects is created and returned holding the calculated number of
	systems.
	
	Inputs:
		p - The map parameter dictionary
		
	Outputs:
		sList - List of Star System Objects
	"""
	
	volume = p["maxX"] * p["maxY"] * (1+p["maxZ"]-p["minZ"])
	nStars = int(round(volume*p["stellarDensity"]))
	sList = []
	for i in range(nStars):
		sList.append(StarSystem(p))
	return sList
	
def findOverlaps(sList):
	mList = []
	mulList = []
	for x in sList:
		mList.append(x.mapPos)
	for x in mList:
		n = mList.count(x);
		if (n>1 and not x in mulList):
			mulList.append(x)
			print ("there are", n,"systems at",x)
	return mulList

def getTweakOffset(sList):
	offset = (0,0)
	largeStarCount = 0
	for s in sList:
		if (sortSpecTypeForDisplay(s)<400):
			largeStarCount = largeStarCount +1
	nStars = len(sList)
	t1 = (getStarOffsetList(nStars))[0]
	temp = (0.5*t1[0],0.5*t1[1])
	
	if (1 == largeStarCount and nStars < 5):
		offset = (-temp[0],-temp[1])
	
	if (2 == largeStarCount and (3 == nStars or 4 == nStars)):
		offset = (0, -temp[1])
		
	if (3 == largeStarCount and (5 == nStars or 4 == nStars)):
		offset = (0, -temp[1])
		
	if (4 == nStars and largeStarCount < 3):
		offset = (-0.5*temp[0],-0.5*temp[1])
		
	if (nStars > 5 and 1 == largeStarCount):
		offset = (-0.5*temp[0],-0.5*temp[1])
		
	if (nStars > 7 and (2 == largeStarCount or 4 == largeStarCount or 5 == largeStarCount)):
		offset = (-0.5*temp[0],-0.5*temp[1])
		
	if ((6 == nStars or 7 == nStars) and 2 == largeStarCount):
		offset = (0,-0.5*temp[1])
		
	if ((6 == nStars or 7 == nStars) and 3 == largeStarCount):
		offset = (temp[0],-0.5*temp[1])
		
	if ((6 == nStars or 7 == nStars) and (4 == largeStarCount or 5 == largeStarCount)):
		offset = (temp[0],0)

	if (nStars > 7  and 3 == largeStarCount):
		offset = (temp[0],-0.5*temp[1])
	
	if (nStars > 7  and (6 == largeStarCount or 7 == largeStarCount)):
		offset = (-0.5*temp[0],0)
	
	return offset

def createMapSymbols(systemList,mList,defDict):
	symbolList = []
	dupList = {}
	systemOffsets = [(0,0),(-30,30),(30,-30),(-30,-30),(30,30)]

	for s in systemList:
		tweakOffset = (0,0)
		dupCount = 0
		# handle mutliple star systems at same (x,y)
		if (s.mapPos in mList):
			if (s.mapPos in dupList.keys()):
				dupCount = dupList[s.mapPos] + 1
			else:
				dupCount = 1
			dupList[s.mapPos] = dupCount
		starOffset = [(0,0)]
		# get list of offset for individual stars in multiple system
		if (s.nStars > 1):
			starOffset = getStarOffsetList(s.nStars)
			tweakOffset = getTweakOffset(s.stars)
		# generate symbol data for each star in system
		xPos = s.mapPos[0]*150+systemOffsets[dupCount][0]+tweakOffset[0]
		yPos = s.mapPos[1]*150+systemOffsets[dupCount][1]+tweakOffset[1]
		data = '<g transform="translate(%f,%f)">' % (xPos,yPos)
		s.drawnPos = (xPos-tweakOffset[0],yPos-tweakOffset[1]) #keep track of where center of system is drawn for later

		i = 0
		starList = sorted(s.stars, key = sortSpecTypeForDisplay)
		for star in starList:
			data += createSymbol(star,starOffset[i],defDict)
			i += 1
		data += '<text x="20" y="20" font-size="20" font-family="Ariel,Helvetica,sans-serif" fill="white">'
		if (s.z > 0):
			data += "+"
		data += "%d</text>" % s.z
		
		
		data += "</g>"
		symbolList.append(data)	
		
	return symbolList

def getStarOffsetList(n):
	"""Offsets for stars in a system
	
	This method returns a list of tuples based on the number of stars
	in the system.  Each tuple represents the x,y offset of the star
	from the system center for drawing purposes.
	
	Input: n - the number of stars in the system
	
	Output: a list of x,y pairs, one for each star in the system
	"""
	if (2 == n):
		return [(-24,-24),(24,24)]
	if (3 == n):
		return [(-36,-36),(36,-20),(-12,36)]
	if (4 == n):
		print ("4 stars")
		return [(-36,-36),(36,-36),(-36,36),(36,36)]
	if (5 == n):
		print ("5 stars")
		return [(-44,-20),(0,-48),(44,-20),(28,32),(-28,32)]
	if (6 == n):
		print ("6 stars")
		return [(-28,-48),(28,-48),(56,0),(28,48),(-28,48),(-56,0)]
	if (7 == n):
		print ("7 stars")
		return [(-28,-48),(28,-48),(56,0),(28,48),(-28,48),(-56,0),(0,0)]
	if (8 == n):
		print ("8 stars")
		return [(-42,-42),(0,-60),(42,-42),(60,0),(42,42),(0,60),(-42,42),(-60,0)]
	if (9 == n):
		print ("9 stars")
		return [(-42,-42),(0,-60),(42,-42),(60,0),(42,42),(0,60),(-42,42),(-60,0),(0,0)]
	if (10 == n):
		print ("10 stars")
		return [(-42,-42),(0,-60),(42,-42),(60,0),(42,42),(0,60),(-42,42),(-60,0),(20,-20),(-20,20)]
	else:
		return [(0,0) * n]
	
def writeMapHeader(f,w,h):
	f.write(r'<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
	f.write("\n")
	f.write(r'<svg xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:cc="http://creativecommons.org/ns#" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 ')
	params = "%u %u" % (w,h)
	f.write(params)
	f.write(r'" xmlns:dc="http://purl.org/dc/elements/1.1/">')
	f.write("\n")
	
def findConnections(sList):
	"""Generate data for system connections
	
	This function looks over the list of stars and
	determines which ones should have connections
	drawn on the map and then calculates the data
	for those connections
	
	Inputs
		sList - List of stellar data
		
	Outputs
		connectionList - List of connection data
	"""
	connectionList = []
	#find "habitable stars"
	hList = []
	for s in sList:
		if s.hasHabitable():
			hList.append(s)
	
	hListSize = len(hList)
	for i in range(hListSize):
		for j in range(i+1,hListSize):
			s1 = hList[i]
			s2 = hList[j]
			p1 = s1.drawnPos
			p2 = s2.drawnPos
			d = sqrt((s1.x-s2.x)*(s1.x-s2.x)+(s1.y-s2.y)*(s1.y-s2.y)+(s1.z-s2.z)*(s1.z-s2.z))
			if (d<15):
				connectionList.append((p1,p2,d))
	
	return connectionList

def drawConnections(f,cList):
	for c in cList:
		#draw the line
		data = '<g><line style="stroke:rgb(255,255,255); stroke-width:5"' 
		data += ' x1="%d" y1="%d" x2="%d" y2="%d" />\n' % (c[0][0],c[0][1],c[1][0],c[1][1])
		#draw the label
		offset = (-45.,-45.);
		xscale = 0.;
		yscale = 0.;
		slope = 0.;
		angle = 0.;
		x1 = float(c[0][0])
		x2 = float(c[1][0])
		y1 = float(c[0][1])
		y2 = float(c[1][1])
		if (x1 != x2): #this would give an infinite slope
			slope = (y1-y2)/(x2-x1)
			angle = atan (-slope) * 180 / acos(-1.)
			xscale = sin (atan (slope) * 2)
			yscale = cos (atan (slope) * 2)
			if (fabs(angle) >= 45.0):
				xscale = -xscale
#				yscale = -yscale
			if (slope < 0):
				xscale = -xscale
#				yscale = -yscale
#			if (slope <= 0): print ("I: sl = %f an = %f xs = %f ys= %f d = %f x1=%f y1=%f x2=%f y2=%f" % (slope,angle,xscale,yscale,c[2],(x1/150),(y1/150),(x2/150),(y2/150)))
		else:
			xscale = -0.2
			yscale = 0
#			if (slope <= 0): print ("I2: sl = %f an = %f xs = %f ys= %f d = %f x1=%f y1=%f x2=%f y2=%f" % (slope,angle,xscale,yscale,c[2],(c[0][0]/150),(c[0][1]/150),(c[1][0]/150),(c[1][1]/150)))
		if (0 == slope):
			yscale /= 2
		else:
			if (fabs(angle) < 10):
				yscale *= 0.8
		xMid = (c[0][0]+c[1][0])/2 + xscale * offset[0]
		yMid = (c[0][1]+c[1][1])/2 + yscale * offset[1]# - (1-yscale) * copysign(20,slope)
#		if (fabs(angle)<10): yMid -= copysign(10,slope)
		data += '<text x="%d" y="%d" font-size="40" font-family="Ariel,Helvetica,sans-serif" fill="white">' % (xMid,yMid)
		data += "%d</text></g>" % c[2]
#		if (fabs(angle) < 20 and fabs(angle) >=10): 
		f.write(data)
#			print ("O: sl = %f an = %f xs = %f ys= %f d = %f x1=%f y1=%f x2=%f y2=%f" % (slope,angle,xscale,yscale,c[2],(c[0][0]/150),(c[0][1]/150),(c[1][0]/150),(c[1][1]/150)))

	
def createMap(params,defDict,symbolList,connectionList):
	f = open(params['filename'],'w')
	# create header
	w = (params['maxX']+1)*150
	h = (params['maxY']+1)*150
	writeMapHeader(f,w,h)
	# add definitions
	writeDefs(f,defDict)
	# add background - Note: we should make the svg canvas black instead
	f.write(' <rect height="%u" width="%u" y="0" x="0" fill="#000"/>\n' %(h,w))
	# add grid
	f.write('<g>\n')
	xMin = 75
	yMin = 75
	xMax = params['maxX']*150 + 75
	yMax = params['maxY']*150 + 75
	for i in range(params['maxX']+1):
		x = i*150+75
		code = '<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke:rgb(100,100,100;stroke-width:5" />' %(x,yMin,x,yMax)
		f.write(code)
	for i in range(params['maxY']+1):
		y = i*150+75
		code = '<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke:rgb(100,100,100;stroke-width:5" />' %(xMin,y,xMax,y)
		f.write(code)
	f.write('</g>\n')
	
	# draw connections and label
	drawConnections(f,connectionList)
	# add star symbols (this comes second so they will be on top)
	writeSymbols(f,symbolList)
	# close off file
	f.write("</svg>")
	f.close()
	

if __name__ == '__main__':
#	seed(3)  # this gives two star systems on the same (x,y) with p = {'maxX':12,'maxY':12,'minZ':-12,'maxZ':12}
#	p = {'maxX':12,'maxY':12,'minZ':-12,'maxZ':12,'stellarDensity':0.004,'filename':"sampleMap.svg"}
	p = {'maxX':44,'maxY':24,'minZ':-12,'maxZ':12,'stellarDensity':0.004,'filename':"sampleMap.svg"
#	p = {'maxX':90,'maxY':100,'minZ':-12,'maxZ':12,'stellarDensity':0.004,'filename':"sampleMap.svg"
		,'datafile':"sampleSystemData.txt"}
	# parse command-line options for size of map, 2D or 3D, grid type, distance threshold and whatever else I think to add

	# generate list of star system data
	#starList = createSystems(p)
	from loadData import loadData
	starList=[]
	connectionList=[]
	loadData("testSystemData.txt",p,starList,connectionList)
	print ("there are",len(starList),"systems on the map")

	# check for overlapping systems and flag
	multipleList = findOverlaps(starList)
	
	defDict = {} # dictionary of gradient definitions for star symbols in SVG file
	# generate symbols for each system
	symbolList = createMapSymbols(starList,multipleList,defDict)
	
	# generate stellar distance data
#	connectionList = findConnections(starList)
	
	# draw map
	createMap(p,defDict,symbolList,connectionList)
	
	#write out the star system data
	from writeData import writeSystemData,writeConnectionData
	writeSystemData(p,starList)
	writeConnectionData(p,connectionList)
