import time
import binaryLoad

class RAM:

    def __init__(self):
        self.size = 256
        self.depth = 8
        self.memory = [0]*self.size

    def __repr__(self):
        pass

    def __str__(self):
        prnt = "-------RAM-------"
        for i,address in enumerate(self.memory):
            if i % 16 == 0:
                prnt += "\n"
            prnt += "{:02x}".format(address)
            prnt += " "
        # for address in self.memory:
        #     adrtuple = divmod(address, 0b10000)
        #
        #     prnt += "\n"
        #     prnt += "{:04b}".format(adrtuple[0])
        #     prnt += " "
        #     prnt += "{:04b}".format(adrtuple[1])
        #     prnt += "  "
        #     prnt += "{:02x}".format(address)
        #     prnt += "  "
        #     prnt += "{:3d}".format(address)
        return prnt
    
    def __getitem__(self, address):
        return self.memory[address]

    def __setitem__(self, address, value):
        value = value % 2**self.depth

        self.memory[address] = value

    def __iter__(self):
        return self.memory


class CPU:

    def __str__(self):
        prnt = self.ram.__str__()
        prnt += "\n"
        prnt += "-------CPU-------"
        for address in [self.regA, self.regB, self.inst]:
            adrtuple = divmod(address, 0b10000)
            
            prnt += "\n"
            prnt += "{:04b}".format(adrtuple[0])
            prnt += " "
            prnt += "{:04b}".format(adrtuple[1])
            prnt += "  "
            prnt += "{:02x}".format(address)
            prnt += "  "
            prnt += "{:3d}".format(address)
        return prnt
    
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
            self.inst = self.read()-1#next clock cycle will be correct
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
            self.regA = self.regA % 2 **self.ram.depth
            return

        if val == 9:
            self.regA = self.regA - self.regB
            self.regA = self.regA % 2 **self.ram.depth
            return

        if val == 10:
            self.inc_inst()
            val = self.read()
            if self.regA:
                self.inst = val
                return
            return
            
        if val == 11:
            self.inc_inst()
            val = self.read()
            if self.regB:
                self.inst = val
                return
            return

    def inc_inst(self):
        self.inst += 1
        if self.inst == self.ram.size:
            self.inst = 0

    def read(self, address = "inst"):
        if address == "inst":
            address = self.inst
        return self.ram[address]

    def write(self, address, value):
        self.ram[address] = value
    
    def clock(self):
        val = self.read()
        
        self.execute(val)
        
        self.inc_inst()


MyRAM = RAM()

MyCPU = CPU(MyRAM)

prgm = binaryLoad.programmer("src.bin")

for i,val in enumerate(prgm):
    MyCPU.write(i, val)


print(MyCPU)
i = 1
while 1:
    MyCPU.clock()
    # if i % 4 == 0:
    print(MyCPU)
    time.sleep(1)
    i += 1






        
