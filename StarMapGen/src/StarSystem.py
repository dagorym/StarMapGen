from random import randint

class StarSystem:
    
    def __init__(self,params):
        self.x = 0
        self.y = 0
        self.z = 0
        self.mapPos = (0,0)
        self.nStars = 0
        self.stars = []
        self.mParams = params
        self.name = "" # star system name
        self._generatePosition()
        self._generateMultiplicity()
        self._generateSpectralType()
        self.drawnPos = (0,0)  # used to know where it was drawn on the map
    
    def _generatePosition(self):
        """Generates random position of star system within x,y,z boundaries
        specified by the map generation parameters
        """
        self.x = randint(1,self.mParams['maxX'])
        self.y = randint(1,self.mParams['maxY'])
        self.z = randint(self.mParams['minZ'],self.mParams['maxZ'])
        self.mapPos = (self.x,self.y)
        self.name = ("OFS-%03d%03d%03d"%(self.x,self.y,self.z))
        
    def _generateMultiplicity(self):
        """Determines the number of stars in the system based on standard
        stellar distribution numbers
        
        This is based on the system multiplicity data from
        
        Need to find paper (thought it was on my thumb drive but it isn't)
        
        and only goes up to 10 stars in a system
        """
        roll = randint(1,1000)
#        roll = 1000
        if (561 > roll):
            self.nStars = 1
        elif (921 > roll):
            self.nStars = 2
        elif (986 > roll):
            self.nStars = 3
        elif (998 > roll):
            self.nStars = 4
        elif (1000 > roll):
            self.nStars = 5
        else:
            r2 = randint(1,1000)
#            r2 = 1000
            if (811 > r2):
                self.nStars = 6
            elif (965 > r2):
                self.nStars = 7
            elif (995 > r2):
                self.nStars = 8
            elif (1000 > r2):
                self.nStars = 9
            else:
                self.nStars = 10
    
    def _getMSSubType(self,spClass):
        """Calculates the spectral subtype (0-9) for main sequence stars.

        This is based roughly on the Kroupa IMF function and could be refined
        """
        roll = randint(1,100)
        set1 = ['A','F','G','K','M']
        if spClass in set1:
            if (9 > roll):
                return spClass+"0"
            elif (18 > roll):
                return spClass+"1"
            elif (27 > roll):
                return spClass+"2"
            elif (36 > roll):
                return spClass+"3"
            elif (46 > roll):
                return spClass+"4"
            elif (56 > roll):
                return spClass+"5"
            elif (67 > roll):
                return spClass+"6"
            elif (78 > roll):
                return spClass+"7"
            elif (89 > roll):
                return spClass+"8"
            else:
                return spClass+"9"
        if (spClass == "B"):
            if (5 > roll):
                return spClass+"0"
            elif (11 > roll):
                return spClass+"1"
            elif (17 > roll):
                return spClass+"2"
            elif (22 > roll):
                return spClass+"3"
            elif (29 > roll):
                return spClass+"4"
            elif (38 > roll):
                return spClass+"5"
            elif (49 > roll):
                return spClass+"6"
            elif (63 > roll):
                return spClass+"7"
            elif (80 > roll):
                return spClass+"8"
            else:
                return spClass+"9"
        if (spClass == "O"):
            if (13 > roll):
                return "O5"
            elif (27 > roll):
                return "O6"
            elif (43 > roll):
                return "O7"
            elif (61 > roll):
                return "O8"
            else:
                return "O9"

                
    def _generateSpectralType(self):
        """Determines the spectral type of each star in the system.
        
        The data generated is stored in the self.stars list and is simply
        a string naming the spectral type of the object
        
        Generation is currently based on the parameters I worked up
        for the original Frontier Space game in 2008.  It should be updated
        to reflect the updated research
        """
        
        for i in range(self.nStars):
            roll = randint(1,100)
#            roll = randint(84,100)
            if (9 > roll):
                self.stars.append("BD")
            elif (83 > roll):
                self.stars.append(self._getMSSubType("M"))
            elif (90 > roll):
                self.stars.append(self._getMSSubType("K"))
            elif (93 > roll):
                self.stars.append(self._getMSSubType("G"))
            elif (95 > roll):
                self.stars.append(self._getMSSubType("F"))
            elif (100 > roll):
                self.stars.append("WD")
            else:
                r2 = randint(1,1000)
                if (584 > r2):
                    self.stars.append(self._getMSSubType("A"))
                elif (667 > r2):
                    self.stars.append(self._getMSSubType("B"))
                elif (1000 > r2): #giants
                    self.stars.append(self._getGiantSpectralType()+"III")
                else:
                    r4 = randint(1,100)
                    if (10 > r4):
                        self.stars.append(self._getMSSubType("O"))
                    elif (100 > r4):
                        self.stars.append(self._getGiantSpectralType()+"I")
                    else:
                        r5 = randint(1,10)
                        if (10 == r5):
                            print ("Made a black hole")
                            self.stars.append("BH")
                        else:
                            print ("Made a neutron star")
                            self.stars.append("NS")

    def _getGiantSpectralType(self):
        """Generates the spectral types for giant and supergiant stars.
        
        The calling function should append the appropriate class identifier
        (i.e. "I" or "III" to the returned value.
        """
        roll = randint(1,100)
        if (83 > roll):
            return "M%d" % randint(0,9)
        elif (90 > roll):
            return "K%d" % randint(0,9)
        elif (93 > roll):
            return "G%d" % randint(0,9)
        elif (95 > roll):
            return "F%d" % randint(0,9)
        else:
            return "K%d" % randint(0,9)
    
    def hasHabitable(self):
        for s in self.stars:
            if ("F" == s[0:1] or "G" == s[0:1] or "K" == s[0:1]):
                return True
        return False
        
if __name__ == '__main__':
    p = {'maxX':10,'maxY':10,'minZ':-5,'maxZ':5}
    x = StarSystem(p)
    print ("position = (",x.x,",",x.y,",",x.z,")")
    print ("map Postion =",x.mapPos)
    print ("nStars =", x.nStars)
    print ("stars =", x.stars,"\n")
    
    y = StarSystem(p)
    print ("position = (",y.x,",",y.y,",",y.z,")")
    print ("map Postion =",y.mapPos)
    print ("nStars =", y.nStars)
    print ("stars =", y.stars)
    
    if (x.mapPos == y.mapPos):
        print ("Overlapping Star Systems")
    
