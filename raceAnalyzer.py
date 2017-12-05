
import re



class RaceAnalyzer():
    
    def __init__(self):  
        try:
            fileName = "lab8input.txt"
            self.count = 0
            self.locDict = { }
            self.typeDict = { "50 Mile Open":[], "50 Mile Masters":[], "100 Mile Open":[], "100 Mile Masters":[] }
            self.nameDict = { }
            with open(fileName,"r") as infile:
                header = infile.readline()   # read in the header
                for line in infile:
                    #print(line)
                    reObj = re.search('\"([^"]+)\".*, (\w{2})\D*(\d+ Mile).*(Open|Masters)\s+[^\s]+\s+([^\s]+)',line)
                    if reObj:
                        self.count += 1
                        self.name = reObj.group(1).title()
                        self.location = reObj.group(2).upper()   # set the state name as upper case
                        self.distance = reObj.group(3)
                        self.subType = reObj.group(4)
                        self.raceType= self.distance + " " + self.subType
                        self.finishTime = reObj.group(5)
                        """
                        print(self.name)
                        print(self.location)
                        print(self.distance)
                        print(self.subType)
                        print(self.raceType)
                        print(self.finishTime)
                        """
                        self.locDict[self.location] = self.locDict.get(self.location, 0)+1
                        self.typeDict[self.raceType].append(self.name)
                        self.nameDict[self.name] = [self.name, self.distance, self.finishTime]
                    """  
                    else:
                        print("############ regex object not found here ############")
                    """
                    #print("**********************************")
        except FileNotFoundError as e:
            print(str(e))
            
            
    def getCount(self):
        return self.count
    
    
    def searchByLocation(self):
        sorted_by_values = [ (key, value) for value, key in sorted([(value, key) for key, value in self.locDict.items()], reverse=True)    ]
        for (key, value) in sorted_by_values :
            print(key, ": ", value)


    def searchByType(self):
        print("50 Mile Distance:")
        print("  Open")
        for name in self.typeDict["50 Mile Open"] : print(name)
        print(str(len(self.typeDict["50 Mile Open"])) + " racers in the 50 mile Open race" )
        
        print("  Masters")
        for name in self.typeDict["50 Mile Masters"] : print(name)
        print(str(len(self.typeDict["50 Mile Masters"])) + " racers in the 50 mile Open race" )
        
        print()  
        
        print("100 Mile Distance:")
        print("  Open")
        for name in self.typeDict["100 Mile Open"] : print(name)
        print(str(len(self.typeDict["100 Mile Open"])) + " racers in the 50 mile Open race" )
        
        print("  Masters")        
        for name in self.typeDict["100 Mile Masters"] : print(name)
        print(str(len(self.typeDict["100 Mile Masters"])) + " racers in the 50 mile Open race" )\
             
    def searchByName(self):
        nameNotFound = True
        while nameNotFound:
            name = input("Enter a racer full name: ").title()
            if name not in self.nameDict:
                print("No racer by the name: " + name)
            else:
                print("Name: " + self.nameDict[name][0])
                print("Distance: "  + self.nameDict[name][1])
                print("Time: "  + self.nameDict[name][2])
                nameNotFound = False


"""
testObj = RaceAnalyzer()
testObj
"""