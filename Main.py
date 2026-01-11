# main.py
from CPU import CPU
from Memory import Memory


def main():
    # ---------------- Initialize machine ----------------
    mem = Memory()
    cpu = CPU(mem)

    # ---------------- Load minimal program ----------------
    # Program:
    #   NOP
    #   HLT
    program = bytes([
        CPU.OP_NOP_IMP,
        CPU.OP_HLT_IMP
    ])

    mem.load_rom(program, start_address=0xF000)

    # ---------------- Manual clocking + trace ----------------
    cpu.step()
    cpu.trace()   # After NOP

    cpu.step()
    cpu.trace()   # After HLT


if __name__ == "__main__":
    main()