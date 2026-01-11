class CPU:
    OP_NOP_IMP = 0x00
    OP_HLT_IMP = 0x01
    OP_LDI_IMM = 0x10

    def __init__(self, mem):
        self.mem = mem
        self.PC  = 0xF000
        self.MAR = 0
        self.MDR = 0
        self.IR  = 0
        self.ACC = 0x00
        self.Z   = 0            # Zero flag (1-bit) 
        self.halted = False     # Halt latch set to False

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

    def fetch(self):
        # Fetch one byte from memory at PC into MDR, then increment PC
        self.MAR = self.PC & 0xFFFF
        self.MDR = self.mem[self.MAR] & 0xFF
        self.PC  = (self.PC + 1) & 0xFFFF
        return self.MDR

    def execute(self):
        if self.IR == self.OP_NOP_IMP:
            pass    # Do nothing

        elif self.IR == self.OP_HLT_IMP:
            self.halted = True  # Set halted to True

        elif self.IR == self.OP_LDI_IMM:
            # Operand fetch (immediate)
            imm = self.fetch()
            self.ACC = imm

            # Update Zero flag based on ACC  
            self.Z = 1 if self.ACC == 0 else 0

        else:
            raise RuntimeError(f"Unknown opcode: {self.IR:02X}")

    def step(self):
        # If halted, ignore clock
        if self.halted:
            return

        # Fetch opcode
        self.IR = self.fetch()

        # Execute
        self.execute()

    def run(self, steps=None):
        if steps is None:
            while not self.halted:
                self.step()
        else:
            for _ in range(int(steps)):
                if self.halted:
                    break
                self.step()
