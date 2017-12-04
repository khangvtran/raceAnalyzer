
import re



class RaceAnalyzer():
    
    def __init__(self):  
        try:
            fileName = "lab8input.txt"
            with open(fileName,"r") as infile:
                header = infile.readline()   # read in the header
                for line in infile:
                    print(line)
                    reObj = re.search('\"([^"]+)\".*, (\w{2})\D*(\d+ Mile).*(Open|Masters)\s+[^\s]+\s+([^\s]+)',line)
                    if reObj:
                        self.name = reObj.group(1)
                        self.location = reObj.group(2).upper()   # set the state name as upper case
                        self.distance = reObj.group(3)
                        self.subType = reObj.group(4)
                        self.raceType= self.distance + " " + self.subType
                        self.finishTime = reObj.group(5)
                        print(self.name)
                        print(self.location)
                        print(self.distance)
                        print(self.subType)
                        print(self.raceType)
                        print(self.finishTime)
                    else:
                        print("############ regex object not found here ############")
                        
                    
                    
                    
                    print("**********************************")
        
        except FileNotFoundError as e:
            print(str(e))
            

testObj = RaceAnalyzer()
testObj
