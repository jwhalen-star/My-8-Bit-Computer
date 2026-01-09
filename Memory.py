class Memory:
    def __init__(self):
        self.data = bytearray(0x10000)  # 64 KB addressable memory

    def __getitem__(self, address): # Return value at an address
        return self.data[address & 0xFFFF]

    def __setitem__(self, address, value):  # Set value at an address
        self.data[address & 0xFFFF] = value & 0xFF

    def load_rom(self, program: bytes, start_address=0xF000):   # Load a program into memory at the specified start address
        start_address &= 0xFFFF
        self.data[start_address:start_address + len(program)] = program
