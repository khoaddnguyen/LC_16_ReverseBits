# input 32-bit of an unsigned integer
# output: integer of the reversed bit above
# The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

def reverseBits(self, n: int) -> int:
    result = 0  # for all 32 bits

    for i in range(32):  # i goes from 0 to 31
        bit = (n >> i) & 1  # shifting right by i and use AND logic
        result = result | (bit << (31 - i))  # logic OR
    return result


