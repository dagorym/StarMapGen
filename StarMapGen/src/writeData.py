def writeSystemData(params,sList):
	f = open(params['datafile'],'w')
	for system in sList:
		f.write('Name: %s\n'%system.name)
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
def writeConnectionData(params,jList):
	f = open(params['datafile'],'a')
	for j in jList:
		f.write('Link: "%s" "%s"\n' % (j[0],j[1]))
	f.write("\n")
	f.close()
