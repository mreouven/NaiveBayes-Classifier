class DataCheck():
    def __init__(self,data):
        self.data=data
        self.not_numeric()

    def is_numeric(self):
        for cle,contenu  in self.data.items():
            #print cle,contenu[0]
            if 'NUMERIC' == contenu[0]:
                1
##                for element in contenu[1]:
##                    try:
##                       element=int(element)
##                    except (TypeError, ValueError):
##                        #print cle
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
