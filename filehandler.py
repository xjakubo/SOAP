import time, os, csv
class FileHandler:

    def __init__(self,semestr):
        self.ktorysemestr = semestr
        self.year = time.strftime("%Y")

        pass

    def makeDirectory(self):
        try:
            os.mkdir('Semestr_%s_%s' %(self.ktorysemestr, self.year))
        except FileExistsError:
            return None

    def csvCreate(self):
        csv.register_dialect('myDialect', delimiter = ',')
        check = os.path.isfile("Semestr_%s_%s/%s.csv" %(self.ktorysemestr, self.year, self.filename))
        if check == False:
            kolumny = ["NR Ucznia", "Srednia"]
            with open("Semestr_%s_%s/%s.csv" %(self.ktorysemestr, self.year, self.filename), "w", newline="") as file:
                writer = csv.writer(file ,dialect='myDialect')
                writer.writerow(kolumny)
                for x in range(1,31):
                    writer.writerow([str(x)])
                file.close()

    def csvRead(self):
        with open("Semestr_%s_%s/%s.csv" %(self.ktorysemestr, self.year, self.filename), "r") as file:
            reader = csv.reader(file, dialect = "myDialect")
            self.content = list(reader)
            file.close()
        pass

    def save(self, filename, numer, srednia):
        row = [str(numer), str(srednia)]
        self.filename = filename
        self.makeDirectory()
        self.csvCreate()
        self.csvRead()
        with open("Semestr_%s_%s/%s.csv" %(self.ktorysemestr, self.year, self.filename), "w", newline="") as file:
            writer = csv.writer(file, dialect='myDialect')
            self.content[numer] = row
            writer.writerows(self.content)
