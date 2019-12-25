
class RAM:

    def __init__(self):
        self.size = 16
        self.memory = [0]*self.size

    def __repr__(self):
        pass

    def __str__(self):
        prnt = "-------RAM-------"
        for address in self.memory:
            prnt += "\n"
            prnt += "{:08b}".format(address)
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
        self.ram = RAM
        

    def execute(self, val):
        if val == 5:
            print(self.inst)

    def inc_inst(self):
        self.inst += 1
        if self.inst == self.ram.size:
            self.inst = 0

    def clock(self):
        val = self.ram[self.inst]

        self.execute(val)
        
        self.inc_inst()


MyRAM = RAM()


MyRAM[4] = 5

MyRAM[10] = 5


MyCPU = CPU(MyRAM)

while 1:
    MyCPU.clock()
    input()
    print("\r", end="")







        
