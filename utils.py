"""
Utility Functions for my crypto exercises.
"""
def xor_strings(a, b, hex=False):
    """XOR two strings"""
    if hex:
        a = a.decode('hex')
        b = b.decode('hex')

    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))


def get_random(size=16):
    """Get random bits with specified size"""
    return open("/dev/urandom").read(size)
