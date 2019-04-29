import re
from StarSystem import StarSystem

def loadData(fName,param,sysList,cList):
    '''loadData opens the file specified by fName and 
    reads in each of the star systems stored in in the file.
    It also requires the parameter object to be passed in (p).
    The function returns a list of StarSystem objects.
    '''
    try:
        f = open(fName,'r')
    except:
        print ("Unable to open file")
        exit(1)

    for line in f:
        #read in system name
        m = re.match('Name:\s*(.*)',line)
#        l = re.match('Link:\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)',line)
        l = re.match('Link: "(.*)" "(.*)"',line)
        if (m):
            s=StarSystem(param) #note that this currently creates a random star system that we will overwrite
            #@todo should probably make a default constructor
            s.name = m.group(1)
    #        print("Name:",s.name)
            #read in coordinates
            line = f.readline()
            p=re.compile(r'(\d+),(\d+),([-]*\d+)')
            m=p.search(line)
            s.x=int(m.group(1))
            s.y=int(m.group(2))
            s.z=int(m.group(3))
            s.mapPos=(s.x,s.y)
    #        print ("Coordinates: ("+s.x+","+s.y+","+s.z+")")
            # read in star count
            line = f.readline()
            m = re.match('Number of Stars: (\d+)',line)
            s.nStars = int(m.group(1))
    #        print("Number of Stars:",s.nStars)
            # read in spectral types
            line = f.readline()
            m = re.match('Spectral Types:\s*(.*)',line)
            s.stars = m.group(1).split(", ")
    #        print ("Spectral Types:",", ".join(str(x) for x in s.stars))
            #read blankline
            line = f.readline()
    #        print (line,end="")
            sysList.append(s)
        elif (l):
#            cList.append(((int(l.group(1)),int(l.group(2))),(int(l.group(3)),int(l.group(4))),int(l.group(5))))
            cList.append((l.group(1),l.group(2)))
        else:
            print ("No Match")
    f.close()
    return sysList
