from tkinter import *
from soap import *

class Window(Frame, Soap):

    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.wyborsemestru()
        self.gui()

    def init_window(self):

        self.master.title("SOAP")
        self.grid()


    def wyborsemestru(self):
        self.pierwszysemestr = Checkbutton(self, text="Pierwszy semestr", command = self.pierwszysemestr)
        self.pierwszysemestr.grid(row = 0, column = 1)
        self.drugisemestr = Checkbutton(self, text = "Drugi semestr", command = self.drugisemestr)
        self.drugisemestr.grid(row = 0, column = 2)

    def gui(self):
        tsprawdzian = Label(self, text = "Sprawdziany")
        tsprawdzian.grid(row = 1, column = 1)
        self.sprawdzian = Entry(self, bd = 5)
        self.sprawdzian.grid(row = 1, column = 2)
        todpowiedzi = Label(self, text = "Odpowiedzi")
        todpowiedzi.grid(row = 2, column = 1)
        self.odpowiedz = Entry(self, bd = 5)
        self.odpowiedz.grid(row = 2, column = 2)
        taktywnosc = Label(self, text = "Aktywnosc")
        taktywnosc.grid(row = 3, column = 1)
        self.aktywnosc = Entry(self, bd = 5)
        self.aktywnosc.grid(row = 3, column = 2)
        tprojekt = Label(self, text = "Projekt")
        tprojekt.grid(row = 4, column = 1)
        self.projekt = Entry(self, bd = 5)
        self.projekt.grid(row = 4, column = 2)
        self.v = StringVar()
        self.v.set("Licz")
        licz = Button(self, textvariable = self.v, width = 20, command = self.licz).grid(row = 6, column = 2)

    def pierwszysemestr(self):
        Soap.__init__(self, 1)
        self.pierwszysemestr.config(state = "disabled")
        self.drugisemestr.config(state = "disabled")

    def drugisemestr(self):
        Soap.__init__(self,2)
        tkoncowy = Label(self, text = "Test koncowy")
        tkoncowy.grid(row = 5, column = 1)
        self.koncowy = Entry(self, bd = 5)
        self.koncowy.grid(row = 5, column = 2)
        self.pierwszysemestr.config(state="disabled")
        self.drugisemestr.config(state = "disabled")

    def licz(self):
        self.clear()
        self.sprawdziany(self.tablica(self.sprawdzian.get()))
        self.odpowiedzi(self.tablica(self.odpowiedz.get()))
        self.aktywnosci(self.tablica(self.aktywnosc.get()))
        self.projekty(self.tablica(self.projekt.get()))
        if self.semestr == 2:
            self.testkoncowy(self.tablica(self.koncowy.get()))
        self.v.set(self.podsumowanie())
root = Tk()
app = Window(root)
root.mainloop()
