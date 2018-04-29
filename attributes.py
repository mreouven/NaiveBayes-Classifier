import os
import csv
import dataCheck
import naivebayes

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
                self.dataex[element[0]]=[]
                self.dataex[element[0]].append(element[1])
            print('Stucture data import success')
        else:
            print "unknow Structure.txt in "+self.chemin
        self.readcsvdata()
    def readcsvdata(self):
        os.chdir(self.chemin)
        if('train.csv' in os.listdir(os.getcwd())): 
            cr = csv.reader(open("train.csv","rb"))
            self.li=[]
            flag=True
            for row in cr:
                if flag:
                    for n in range(0,len(row)):
                        self.li.append([])
                    flag=False
                for n in range(0,len(row)):
                    self.li[n].append(row[n])
        print('CSV data import success')
        self.attachement()
    def attachement(self):
        if self.li and self.dataex:
            for element in self.li:
                #self.dataex[element.pop(0)].append([1,3])
                self.dataex[element.pop(0)].append(element)
        print('Attachement success')
        self.chekdata()
    def chekdata(self):
        datan=dataCheck.DataCheck(self.dataex,3)
        self.dataex=datan.data
        
da=readDATA('C:/Users/mreou/Documents/GitHub/Naive-Bayes')
n=naivebayes.NaiveBayes(da.dataex,3)
