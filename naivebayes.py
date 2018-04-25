class NaiveBayes():
    def __init__(self,data):
        self.data=data
        self.proba={}
        self.findmyclass()
        self.setproba()
    def findmyclass(self):
        self.classe=self.data.pop('class')
        self.classe.append({'yes':self.classe[1].count('yes'),'no':self.classe[1].count('no'),'pyes':float(self.classe[1].count('yes'))/float(len(self.classe[1])),'pno':float(self.classe[1].count('no'))/float(len(self.classe[1]))})
    def setproba(self):
        for cle,contenu  in self.data.items():
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
                    self.proba[cle][e]['yes']=countyes
                    self.proba[cle][e]['no']=countno
                    self.proba[cle][e]['pyes']=float(countyes)/float(self.classe[2]['yes'])
                    self.proba[cle][e]['pno']=float(countno)/float(self.classe[2]['no'])
        #print self.proba
                                
                        
                    
                
                
