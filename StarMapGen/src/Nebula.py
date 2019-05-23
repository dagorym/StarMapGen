from sys import maxsize

class Nebula:
	def __init__(self):
		self.cells = []
		self.boundary = []
		
	def loadData(self,data):
		if (data[0:7] != "Nebula:"):
			print ("bad data")
			return
		print ("Good data string")
		pairs = data[9:-1].split("),(")
		for p in pairs:
			vals = p.split(",")
			self.cells.append((int(vals[0]),int(vals[1])))
		
	def printCells(self):
		for c in self.cells:
			print (c)

	def findBoundary(self):
		#find the left most cell on the upper row
		y = maxsize
		for c in self.cells:
			if (c[1] < y):
				y = c[1]
		x = maxsize
		for c in self.cells:
			if (c[1] == y and c[0] < x):
				x = c[0]
		# now find the boundary path
		self._nextCell((x,y),(x,y),"S",[])

	def _nextCell(self,start,current,dir,visited):
		if (current not in self.cells): return
		self.boundary.append((current,dir))
		visited.append((current,dir))
		if (current == start and dir != "S"): return
		x = current[0]
		y = current[1]
		# try order is right, down, left, up
		if (((x+1,y),"R") not in visited): 
			self._nextCell(start,(x+1,y),"R",visited)
		if (((x,y+1),"D") not in visited): 
			self._nextCell(start,(x,y+1),"D",visited)
		if (((x-1,y),"L") not in visited): 
			self._nextCell(start,(x-1,y),"L",visited)
		if (((x,y-1),"U") not in visited): 
			self._nextCell(start,(x,y-1),"U",visited)
		

if __name__ == '__main__':
	data = "Nebula: (2, 1),(2, 2),(1,2),(3,2)"
	n = Nebula()
	n.loadData(data)
	n.printCells()
	n.findBoundary()
	print (n.boundary)
