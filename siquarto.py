
import time

class Quarto:
    def __init__(self,stan_planszy,pionki_zuzyte,pionki_dostepne,dostepne_pola):
        if stan_planszy is None:
            print("None")
            self.pionki_wszystkie = ["{0:04b}".format(x) for x in range(16)]
            self.pionki_zuzyte=[]
            self.pionki_dostepne=self.pionki_wszystkie
            self.dostepne_pola=[0,1,2,3,4,5,6,7,8,9,10,11,12,14,15]
            self.stan_planszy=[]
            for x in range(16):
                self.stan_planszy.append("")
        else:
            print("Not none")
            self.pionki_wszystkie = ["{0:04b}".format(x) for x in range(16)]
            self.pionki_zuzyte=pionki_zuzyte
            self.pionki_dostepne=pionki_dostepne
            self.dostepne_pola=dostepne_pola
            self.stan_planszy=stan_planszy
            

    """
    0-1011
    1-0111
    2 0100
    3 1110
    4 0110
    5 1100
    6 0010
    7 
    8 1001
    9 1111
    10 0101 #
    11 
    12 1101
    13 1010
    14 0011
    15 1000
     dostepne:
     0001
     0000



    Zasady quarto:
    Rodzaje pionk�w
    -Rozmiar wysoki/niski
    -Kolor  bia�y/czarny
    -Kszta�t kwadratowy/owalny
    -Wkl�s�o�� wkl�s�y/wypuk�y

    """
    
    """
    stan_planszy:
    0,1,2,3
    4,5,6,7
    8,9,10,11
    12,13,14,16
    """    

    #funkcja wykonujaca ruch i sprawdzajaca czy jest mozliwy
    def zrobRuch(self,pionek,pole):
        for pioneksprawdzany in self.pionki_zuzyte:
            if pionek==pioneksprawdzany:            
                print("Podany pionek zostal juz wykorzystany")
                return -1
        if self.stan_planszy[pole]!='':
            return -1
        self.stan_planszy[pole]=pionek
        self.pionki_zuzyte.append(pionek)
        self.pionki_dostepne.remove(pionek)
        self.dostepne_pola.remove(pole)     
        return self.stan_planszy
    #https://www.youtube.com/watch?v=fInYh90YMJU

    # https://github.com/sondreluc/Quarto/tree/master/src/QuartoGame
        
    #sprawdza czy wygrales po podaniu pola na ktory polozyles pionek
    def czyWygrana(self,pole):
        kolumna=pole%4
        wiersz=int(pole/4)
        pionki=[]
        #przekatna 1
        if pole%3==0:
            for i in range(4):
                element=self.stan_planszy[3*(i+1)]
                if element =='':
                    break
                pionki.append(element)
            if len(pionki)==4:
                if self.sprawdzCechy(pionki):
                    return True
        #przekatna2
        pionki.clear()    
        if pole%5 ==0:
            for i in range(4):
                x=self.stan_planszy
                element=self.stan_planszy[i*5]
                if element =='':
                    break
                pionki.append(element)
            if len(pionki)==4:
                if self.sprawdzCechy(pionki):
                    return True
        #pion
        pionki.clear()
        for i in range(4):
            element=self.stan_planszy[kolumna+i*4]
            if element =='':
                break
            pionki.append(element)
        if len(pionki)==4:
            if self.sprawdzCechy(pionki):
                return True
        #poziom
        pionki.clear()
        for i in range(4):
            element=self.stan_planszy[wiersz*4+i]
            if element =='':
                break
            pionki.append(element)
        if len(pionki)==4:
            if self.sprawdzCechy(pionki):
                return True
        return False

    #sprawdza czy wskazane 4 pionki posiadaja ta sam� cech�
    def sprawdzCechy(self,pionki=[]):

        if len(pionki)==0:
            return False
        for bitindex in range(4):
            czterytakiesame=False
            for pionekindex in range (3):
                if not (int(pionki[pionekindex][bitindex])^int(pionki[pionekindex+1][bitindex]))==0:
                    czterytakiesame=False
                    break
                else:
                    czterytakiesame=True
            if(czterytakiesame):
                #print("Cztery takie same cechy")
                return True
        #print("Brak 4 takich samych cech")
        return False


"""
ktozaczyna=False gracz
ktozaczyna=True bot
"""

counter=0
counter1=0

class Node:    
    
    def __init__(self,stan_planszy,pionki_zuzyte,pionki_dostepne,dostepne_pola,pionek,poziom,czyjakolej):
        global counter
        global counter1
        self.poziom=poziom
        self.q=Quarto(stan_planszy,pionki_zuzyte,pionki_dostepne,dostepne_pola)
        self.pionek=pionek
        self.wezly=[]
        self.czyjakolej=czyjakolej

        tabbuf=list(self.q.dostepne_pola)
        tabbuf2=list(self.q.pionki_dostepne)
        tabbuf2.remove(pionek)#usunięcie pionka wybranego przez gracza
        if tabbuf2 == []:
            counter=counter+1

        for pole in tabbuf:
            w=Quarto(list(stan_planszy),list(pionki_zuzyte),list(pionki_dostepne),list(dostepne_pola))
            tab3=list(tabbuf)
        #if w.zrobRuch(pionek,pole)!= -1:
        #    if w.czyWygrana(pole):  
        #        print("Cztery takie same cechy")              
            #print(pionek,"odebrany")
            #print(w.pionki_dostepne)
            #print(w.pionki_dostepne)                       
            #print(w.stan_planszy)
            tab3.remove(pole)
            counter1=counter1+1

            for pion in tabbuf2:
                    counter1=counter1+1
                    #        #break
                    #    else:
                    #        print("Brak czterech takich samych cech")
                    #print(pion,"wysylany")
                    #print(tabbuf2,"tabbuf2") 
                    #print(w.pionki_dostepne)  
                    #print()
                    tab4=list(tabbuf2)                                        
                    self.wezly.append(Node(list(w.stan_planszy),list(w.pionki_zuzyte),tab4,tab3,pion,self.poziom+1, not czyjakolej))
                    #print("o")
        if dostepne_pola==[]:
            counter=counter+1       
      
        if len(tabbuf):
            print("petla zerowa")

            



#testy

root=Quarto(None,None,None,None)
root.pionki_zuzyte=["1011",
    "0111",
    "0100",
    "1110",
    "0110",
    "1100",
    "0010",
    "1001",
    "1111",
    "1101",
    "1010",
    "0011",
    "1000"]
root.pionki_dostepne=["0001","0000","0101"]
root.dostepne_pola=[7,10,11]
pionek="0101"
pole=10

root.stan_planszy=["1011",
    "0111",
    "0100",
    "1110",
    "0110",
    "1100",
    "0010",
    "",
    "1001",
    "1111",
    "",
    "",
    "1101",
    "1010",
    "0011",
    "1000"]

"""
root.zrobRuch(pionek,pole)
print(root.czyWygrana(pole))
"""
Node(root.stan_planszy,root.pionki_zuzyte,root.pionki_dostepne,root.dostepne_pola,pionek,0,True)
print(counter)
print(counter1)