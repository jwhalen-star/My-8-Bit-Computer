# main.py
from CPU import CPU
from Memory import Memory

def main():
    # ---------------- Initialize machine ----------------
    mem = Memory()
    cpu = CPU(mem)

    # ---------------- Load minimal implied-mode program ----------------
    # Program:
    #   NOP
    #   NOP
    #   NOP
    #   HLT
    program = bytes([
        CPU.OP_NOP_IMP,
        CPU.OP_NOP_IMP,
        CPU.OP_NOP_IMP,
        CPU.OP_HLT_IMP
    ])

    mem.load_rom(program, start_address=0xF000)

    # ---------------- Run multiple steps with trace ----------------
    cpu.trace_enabled = True
    cpu.run(steps=10)   # Stops automatically when HLT executes

if __name__ == "__main__":
    main()
