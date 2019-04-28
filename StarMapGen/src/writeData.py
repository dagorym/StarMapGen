def writeSystemData(params,sList):
	f = open(params['datafile'],'w')
	for system in sList:
		f.write('Name:\n')
		f.write("Coordinates: (%d,%d,%d)\n" % (system.x,system.y,system.z))
		f.write("Number of Stars: %d\n" % system.nStars)
		f.write("Spectral Types: ")
		count = 0
		for star in system.stars:
			f.write(star)
			count = count + 1
			if (count != system.nStars):
				f.write(", ")
			else:
				f.write("\n\n")
	
	f.close()

# This function is currently working with the "drawn" coordinates.
# @todo need to adjust everything to use "real" coordinates and map to "drawn"
def writeConnectionData(params,cList):
	f = open(params['datafile'],'a')
	for c in cList:
		f.write("Link: %d %d %d %d %d\n" % (c[0][0],c[0][1],c[1][0],c[1][1],c[2]))
	f.write("\n")
	f.close()
