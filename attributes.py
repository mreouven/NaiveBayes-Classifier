import os
for filename in os.listdir(os.getcwd()):
    print filename

class readDATA:
    def __init__(self,chemin):
        if(isinstance(chemin,str)):
            self.chemin=chemin
            self.dataex={}
            self.readStruct()
    def readStruct(self):
        os.chdir(self.chemin)
        if('Structure.txt' in os.listdir(os.getcwd())):
            text_file = open("Structure.txt", "r")
        lines = text_file.readlines()
        text_file.close()
        data=[]
        for element in lines:
            data.append(element.split())

        for element in data:
            element.remove('@ATTRIBUTE')
            if element[1] != 'NUMERIC':
                element[1]=element[1].replace('{','')
                element[1]=element[1].replace('}','')
                element[1]=element[1].split(',')
      
        for element in data:
            self.dataex[element[0]]=element[1]
        







