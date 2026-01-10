class CPU:
    OP_NOP_IMP = 0x00
    OP_HLT_IMP = 0x01

    def __init__(self, mem):
        self.mem = mem
        self.PC  = 0xF000
        self.MAR = 0
        self.MDR = 0
        self.IR  = 0

    def trace(self):
        print(
            f"PC={self.PC:04X} "
            f"IR={self.IR:02X} "
            f"MAR={self.MAR:04X} "
            f"MDR={self.MDR:02X}"
        )

    def execute(self):
        if self.IR == self.OP_NOP_IMP:
            pass    # Do nothing

    def step(self):
        # Fetch
        self.MAR = self.PC & 0xFFFF
        self.MDR = self.mem[self.MAR] & 0xFF
        self.IR  = self.MDR
        self.PC  = (self.PC + 1) & 0xFFFF

        # Execute
        self.execute()

    def run(self, steps=None):
        if steps is None:
            while True:
                self.step()
        else:
            for _ in range(int(steps)):
                self.step()
