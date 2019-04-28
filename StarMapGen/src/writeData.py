def writeSystemData(params,sList,connectionList):
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

