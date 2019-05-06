
from filehandler import *

class Soap(FileHandler):

    def __init__(self, semestr):
        self.semestr = semestr
        self.oceny = []
        FileHandler.__init__(self, self.semestr)



    def clear(self):
        self.oceny.clear()
        self.srednia = 0

    def tablica(self, znaki):
        tablica = znaki.split(" ")
        return list(map(float, tablica))

    def sprawdziany(self, tablica):
        wynik = sum(tablica)/len(tablica)
        if self.semestr == 1:
            self.oceny.append(wynik*0.5)
        else:
            self.oceny.append(wynik*0.4)

    def odpowiedzi(self,tablica):
        wynik = sum(tablica)/len(tablica)
        self.oceny.append(wynik*0.2)

    def aktywnosci(self,tablica):
        wynik = sum(tablica)/len(tablica)
        self.oceny.append(wynik*0.2)

    def projekty(self,tablica):
        wynik = sum(tablica)/len(tablica)
        self.oceny.append(wynik*0.1)

    def testkoncowy(self,tablica):
        wynik = sum(tablica)/len(tablica)
        self.oceny.append(wynik*0.1)

    def podsumowanie(self):
        self.srednia = round(sum(self.oceny),2)
        return self.srednia
