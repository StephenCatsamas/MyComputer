import csv

class programmer:
    def __init__(self, file):

        self.fp = file
        self.values = list()
        with open(self.fp, newline="") as csvfile:
            self.reader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in self.reader:
                str = row[0].strip().replace(" ", "")
                self.values.append( eval(str))

    def __iter__(self):
        return iter(self.values)
