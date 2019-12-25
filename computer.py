import time


class RAM:

    def __init__(self):
        self.size = 16
        self.memory = [0]*self.size

    def __repr__(self):
        pass

    def __str__(self):
        prnt = "-------RAM-------"
        for address in self.memory:
            addresshigh = address//16
            addresslow = address - addresshigh
            
            prnt += "\n"
            prnt += "{:04b}".format(addresshigh)
            prnt += " "
            prnt += "{:04b}".format(addresslow)
            prnt += "  "
            prnt += "{:02x}".format(address)
            prnt += "  "
            prnt += "{:3d}".format(address)
        return prnt
    
    def __getitem__(self, address):
        return self.memory[address]

    def __setitem__(self, address, value):
        self.memory[address] = value

    def __iter__(self):
        return self.memory


class CPU:
    
    def __init__(self, RAM):
        self.regA = 0b0
        self.regB = 0b0
        self.inst = 0b0
        self.exef = 0b0
        self.ram = RAM
        

    def execute(self, val):
        if val == 0:
            return

        if val == 1:
            self.inc_inst()
            self.inst = self.read()
            return

        if val == 2:
            self.inc_inst()
            val = self.read()
            self.regA = self.read(val)
            return

        if val == 3:
            self.inc_inst()
            val = self.read()
            self.regB = self.read(val)
            return

        if val == 6:
            self.inc_inst()
            val = self.read()
            self.write(val, self.regA)
            return

        if val == 7:
            self.inc_inst()
            val = self.read()
            self.write(val, self.regB)
            return

        if val == 8:
            self.regA = self.regA + self.regB
            return

        if val == 9:
            self.regA = self.regA - self.regB
            return

        if val == 10:
            self.inc_inst()
            val = self.read()
            if self.regA:
                self.inst = val
                return
            
        if val == 11:
            self.inc_inst()
            val = self.read()
            if self.regB:
                self.inst = val
                return

    def inc_inst(self):
        self.inst += 1
        if self.inst == self.ram.size:
            self.inst = 0

    def read(self, address = self.inst):
        return self.ram[address]

    def write(self, address, value):
        self.ram[address] = value
    
    def clock(self):
        val = self.read()
        
        self.execute(val)
        
        self.inc_inst()


MyRAM = RAM()


MyRAM[5] = 1

MyRAM[6] = 3

print(MyRAM)


MyCPU = CPU(MyRAM)

while 1:
    MyCPU.clock()
    time.sleep(1)







        
