from sys import getsizeof

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # Start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # Shift left two bits
            
            if nucleotide == "A":  # Change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":  # Change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # Change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # Change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # Get just 2 relevant bits
            if bits == 0b00: # Same as A
                gene += "A"
            elif bits == 0b01: # Same as C
                gene += "C"
            elif bits == 0b10: # Same as G
                gene += "G"
            elif bits == 0b11: # Same as T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1] # Reverse string by slicing backwards

    def __str__(self) -> str: # String representation for pretty printing
        return self.decompress()

if __name__ == "__main__":
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # Compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # Decompress
    print("original is the same as decompressed: {}".format(original == compressed.decompress()))
