import csv

class programmer:
    def __init__(self, file):

        self.fp = file
        self.values = [0]*256
        self.counter = 0
        with open(self.fp, newline="") as csvfile:
            self.reader = csv.reader(csvfile, delimiter=";", quotechar="|")
            for row in self.reader:
                self.interpret(row)

    def __iter__(self):
        return iter(self.values)

    def interpret(self, row):
        print(row)
        try:
            row[0]
        except IndexError:
            return None

        if row[0].strip() == "CMD":
            if row[1].strip() == "ADR":
                self.counter = eval(row[2].strip().replace(" ", ""))
                return None

        str = row[0].strip().replace(" ", "")
        self.values[self.counter] = eval(str)
        self.counter += 1