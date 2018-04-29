class DataCheck():
    def __init__(self,data,dis_bin):
        self.data=data
        self.dis_bin=dis_bin
        self.not_numeric()
        self.is_numeric()

    def is_numeric(self):
        for cle,contenu  in self.data.items():
            if 'NUMERIC' == contenu[0]:
                for i in range(0,len(contenu[1])):
                    try:
                        contenu[1][i]=int(contenu[1][i])
                    except (TypeError, ValueError):
                        1
        for cle,contenu  in self.data.items():
            if 'NUMERIC' == contenu[0]:
                averages=average(contenu[1])
                for i in range(0,len(contenu[1])):
                    try:
                        #print contenu[1][i]
                        contenu[1][i]=int(contenu[1][i])
                    except (TypeError, ValueError):
                        contenu[1][i]=averages
            
        print "Value is_numeric success"

            
    def not_numeric(self):
        for cle,contenu  in self.data.items():
            if 'NUMERIC' != contenu[0]:
                count=0
                ide=''
                for element in contenu[0]:
                    if count<contenu[1].count(element):
                        count=contenu[1].count(element)
                        ide=element
                for i in range(0,len(contenu[1])):
                    if contenu[1][i] not in contenu[0]:
                        contenu[1][i]=ide
        print "Value not_numeric success"
        
def average(liste):
    som=0
    for i in range(0,len(liste)):
        try:
            som+=liste[i]
        except (TypeError, ValueError):
            1
    return som/len(liste)
