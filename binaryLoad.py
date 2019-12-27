import csv

class programmer:

    opcodes = { 
            "NOP": 0x00,
            "GTO": 0x01,
            "LDA": 0x02,
            "LDB": 0x03,
            "WRA": 0x06,
            "WRB": 0x07,
            "ADD": 0x08,
            "SUB": 0x09,
            "IFA": 0x0a,
            "IFB": 0x0b
            }
    lables = dict()

    def __init__(self, file):

        self.fp = file
        self.values = [0]*256
        self.counter = 0
        self.cont = list()
        with open(self.fp, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";", quotechar="|")
            for row in reader:
                self.cont.append(row)
            for row in self.cont:
                self.get_lables(row)
            self.counter = 0
            for row in self.cont:
                self.interpret(row)

    def __iter__(self):
        return iter(self.values)

    def get_lables(self,row):
        print(row)
        try:
            row[0]
        except IndexError:
            return None

        rstrp = row[0].strip()

        if row[0].strip() == "":
            return None
            
        if rstrp == "CMD":
            if row[1].strip() == "ADR":
                self.counter = eval(row[2].strip().replace(" ", ""))
                return None
            if row[1].strip() == "ADA":
                self.counter += eval(row[2].strip().replace(" ", ""))
                return None
            if row[1].strip() == "ADM":
                self.counter -= eval(row[2].strip().replace(" ", ""))
                return None
            return None
            
        if rstrp == "LAB":
            if row[1].strip() == "DEF":
                programmer.lables[row[2].strip()] = self.counter
                return None

        if rstrp in programmer.opcodes:
            self.counter += 1
            return None

        self.counter += 1

    def interpret(self, row):
        print(row)
        try:
            row[0]
        except IndexError:
            return None

        rstrp = row[0].strip()

        if row[0].strip() == "":
            return None

        if rstrp == "CMD":
            if row[1].strip() == "ADR":
                self.counter = eval(row[2].strip().replace(" ", ""))
                return None
            if row[1].strip() == "ADA":
                self.counter += eval(row[2].strip().replace(" ", ""))
                return None
            if row[1].strip() == "ADM":
                self.counter -= eval(row[2].strip().replace(" ", ""))
                return None
            return None
        
        if rstrp == "LAB":
            if row[1].strip() == "REC":
                self.values[self.counter] = programmer.lables[row[2].strip()]
                self.counter += 1
                return None
            return None

        if rstrp in programmer.opcodes:
            self.values[self.counter] = programmer.opcodes[rstrp]
            self.counter += 1
            return None
            
        str = rstrp.replace(" ", "")
        self.values[self.counter] = eval(str)
        self.counter += 1