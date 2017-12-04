
import re



class raceAnalyzer():
    
    def __init__(self):  
        try:
            fileName = "lab8input_test.txt"
            with open(fileName,"r") as infile:
                header = infile.readline()   # read in the header
                for line in infile:
                    print(line)
                    reObj = re.search('(\"[^"]+\").*, (\w{2})\D*(\d+ Mile)',line)
                    #print(reObj.group(3))
                    
                    self.name = reObj.group(1)
                    self.location = reObj.group(2).upper()   # set the state name as upper case
                    self.distance = reObj.group(3)
                    print(self.name)
                    print(self.location)
                    print(self.distance)
                    
                    
                    
                    print("**********************************")
        
        except FileNotFoundError as e:
            print(str(e))
            

testObj = raceAnalyzer()
testObj