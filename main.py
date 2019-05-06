from tkinter import *
from soap import *

class Window(Frame, Soap):

    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()
        self.wyborSemestru()

    def initWindow(self):

        self.master.title("SOAP")
        self.grid()
        self.v = StringVar(self, value = "Licz")
        self.nr = StringVar(self, value = "Nr Ucznia")
        self.klasa = StringVar(self, value = "Klasa")


    def wyborSemestru(self):
        self.pierwszysemestr = Checkbutton(self, text="Pierwszy semestr", command = self.pierwszysemestr)
        self.pierwszysemestr.grid(row = 0, column = 1)
        self.drugisemestr = Checkbutton(self, text = "Drugi semestr", command = self.drugisemestr)
        self.drugisemestr.grid(row = 0, column = 2)

    def gui(self):
        Label(self, text = "Sprawdziany").grid(row = 1, column = 1)
        self.sprawdzian = Entry(self, bd = 5)
        self.sprawdzian.grid(row = 1, column = 2)
        Label(self, text = "Odpowiedzi").grid(row = 2, column = 1)
        self.odpowiedz = Entry(self, bd = 5)
        self.odpowiedz.grid(row = 2, column = 2)
        Label(self, text = "Aktywnosc").grid(row = 3, column = 1)
        self.aktywnosc = Entry(self, bd = 5)
        self.aktywnosc.grid(row = 3, column = 2)
        Label(self, text = "Projekt").grid(row = 4, column = 1)
        self.projekt = Entry(self, bd = 5)
        self.projekt.grid(row = 4, column = 2)
        Button(self, textvariable = self.v, width = 20, command = self.licz).grid(row = 6, column = 1, columnspan = 2, sticky = W+E)
        self.nrklasy = Entry(self, textvariable = self.klasa, width = 19)
        self.nrklasy.grid(row = 7, column = 1)
        self.nrucznia = Entry(self, textvariable = self.nr, width = 19)
        self.nrucznia.grid(row = 7, column = 2)
        Button(self, text = "Zapisz Wynik", width = 20, command = self.zapisz).grid(row = 8, column = 1, columnspan = 2, sticky = W+E)
    def pierwszysemestr(self):
        self.gui()
        Soap.__init__(self, 1)
        self.pierwszysemestr.config(state = "disabled")
        self.drugisemestr.config(state = "disabled")

    def drugisemestr(self):
        self.gui()
        Soap.__init__(self,2)
        Label(self, text = "Test koncowy").grid(row = 5, column = 1)
        self.koncowy = Entry(self, bd = 5)
        self.koncowy.grid(row = 5, column = 2)
        self.pierwszysemestr.config(state="disabled")
        self.drugisemestr.config(state = "disabled")

    def zapisz(self):
        self.save(self.nrklasy.get(), self.nrucznia.get(), self.licz())
        pass

    def licz(self):
        try:
            self.clear()
            self.sprawdziany(self.tablica(self.sprawdzian.get()))
            self.odpowiedzi(self.tablica(self.odpowiedz.get()))
            self.aktywnosci(self.tablica(self.aktywnosc.get()))
            self.projekty(self.tablica(self.projekt.get()))
        except ValueError:
            self.v.set("Blad!")
            return 0
        if self.semestr == 2:
            self.testkoncowy(self.tablica(self.koncowy.get()))
        self.v.set(self.podsumowanie())
        return self.podsumowanie()
root = Tk()
app = Window(root)
root.mainloop()
