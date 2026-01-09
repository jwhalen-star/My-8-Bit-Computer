class CPU:
    OP_NOP_IMP = 0x00

    def __init__(self, mem):
        self.mem = mem
        self.PC  = 0xF000
        self.MAR = 0
        self.MDR = 0
        self.IR  = 0

    def execute(self):
        if self.IR == self.OP_NOP_IMP:
            pass

    def step(self):
        # Fetch
        self.MAR = self.PC & 0xFFFF
        self.MDR = self.mem[self.MAR] & 0xFF
        self.IR  = self.MDR
        self.PC  = (self.PC + 1) & 0xFFFF

        # Execute
        self.execute()