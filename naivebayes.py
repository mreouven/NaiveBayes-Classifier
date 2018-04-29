class NaiveBayes():
    def __init__(self,data,binSelect):
        self.data=data
        self.binSelect=binSelect
        self.proba={}
        self.findmyclass()
        self.setbinSelection()
        self.setproba()
        self.calculatorNB()
    def findmyclass(self):
        self.classe=self.data.pop('class')
        self.classe.append({'yes':self.classe[1].count('yes'),'no':self.classe[1].count('no'),'pyes':float(self.classe[1].count('yes'))/float(len(self.classe[1])),'pno':float(self.classe[1].count('no'))/float(len(self.classe[1]))})
    def setproba(self):
        for cle,contenu  in self.data.items():
            #laplace ajouter +1 jan feb ....
            if 'NUMERIC' != contenu[0]:
                self.proba[cle]={}
                for e in contenu[0]:
                    countyes=0
                    countno=0
                    for i in range(0,len(contenu[1])):
                        if contenu[1][i]==e:
                            #print contenu[1][i],self.classe[1][i]
                            if self.classe[1][i]=='yes':
                                countyes+=1
                            if self.classe[1][i]=='no':
                                countno+=1
                    self.proba[cle][e]={}
                    #Laplace Smoothing
                    countyes+=1
                    countno+=1
                    self.proba[cle][e]['yes']=countyes
                    self.proba[cle][e]['no']=countno
                    self.proba[cle][e]['pyes']=float(countyes)/float(len(contenu[1]))
                    self.proba[cle][e]['pno']=float(countno)/float(len(contenu[1]))
    def setbinSelection(self):
        for cle,contenu  in self.data.items():
            if 'NUMERIC' == contenu[0]:
                binInstance=(max(contenu[1])+min(contenu[1]))/self.binSelect
                #print(binInstance)
                for i in range(0,len(contenu[1])):
                    1    

    def calculatorNB(self):
        self.result={'yes':0,'no':0}
        for a,b in self.proba.items():
            for i,j in b.items():
                if self.result['yes'] == 0:
                    self.result['yes']=j['pyes']
                else:
                    self.result['yes']*=j['pyes']
                if self.result['no']== 0:
                    self.result['no']=j['pno']
                else:
                    self.result['no']*=j['pno']
        
                                
                        
                    
                
                
