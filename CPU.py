class CPU:
    OP_NOP_IMP = 0x00   # Implied NOP opcode
    OP_HLT_IMP = 0x01   # Implied HLT opcode
    OP_LDI_IMM = 0x10   # Load Immediate opcode

    def __init__(self, mem):
        self.mem = mem  # Provides a reference to the memory of the machine
        self.PC  = 0xF000   # Program Counter initialized to first address of ROM
        self.MAR = 0    # Memory Address Register initialized to 0
        self.MDR = 0    # Memory Data Register initialized to 0
        self.IR  = 0    # Instruction Register initialized to 0
        self.ACC = 0x00  # Accumulator initialized to 0
        self.Z   = 0    # Zero flag initialized to 0
        self.halted = False     # Halt latch set to False
        self.trace_enabled = False  # Trace flag by default set to False

    def trace(self):
        print(
            f"PC={self.PC:04X} "
            f"IR={self.IR:02X} "
            f"ACC={self.ACC:02X} "
            f"Z={self.Z} "               
            f"MAR={self.MAR:04X} "
            f"MDR={self.MDR:02X} "
            f"HALT={int(self.halted)}"
        )

    def fetch(self):    # Fetch one byte from memory at PC into MDR, then increment PC
        self.MAR = self.PC & 0xFFFF # Load address from PC into MAR
        self.MDR = self.mem[self.MAR] & 0xFF    # Read byte from memory into MDR
        self.PC  = (self.PC + 1) & 0xFFFF   # Increment PC
        return self.MDR # Returns the fetched byte

    def execute(self):
        if self.IR == self.OP_NOP_IMP:  # Instruction to "do nothing"
            pass    # "Do nothing"

        elif self.IR == self.OP_HLT_IMP:    # Instruction which can halt the CPU
            self.halted = True  # Sets halt variable to True

        elif self.IR == self.OP_LDI_IMM: # Immediate operand fetch, loads value into ACC
            imm = self.fetch()
            self.ACC = imm
 
            self.Z = 1 if self.ACC == 0 else 0  # Updates Zero flag based on value loaded to ACC 

        else:
            raise RuntimeError(f"Unknown opcode: {self.IR:02X}")    # Raise error if opcode is unknown

    def step(self):
        if self.halted: # Halts function of CPU if halted is True
            return

        self.IR = self.fetch()  # Fetches opcode to IR

        self.execute()  # Executes instruction behavior

        if self.trace_enabled:
            self.trace()  # Trace if enabled

    def run(self, steps=None):
        if steps is None:   # Indefinite run
            while not self.halted:
                self.step()

        else:
            for _ in range(int(steps)): # Run a fixed number of instruction steps
                if self.halted:
                    break
                self.step()
