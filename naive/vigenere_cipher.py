"""
Vigenere Cipher

The vigenere cipher is a symmetric key cipher that operates as a group of
Caesar ciphers in sequence with different rotations:

    KEY         == boomboombo
    MESSAGE     == helloworld
    CIPHERTEXT  == jvopbrfqba

This cipher is crackable in a few ways but most notably it is known to have
repeating bits across a ciphertext which give away the blocks of the original
key. When you know how long a key is and the ciphertext of that key, all that
you have to do is run a Caesar cipher on each block until you break the code.

This does however help some against frequency attacks as letters don't
correspond as well.

The basic formula is as follows:
    E(m) = ((m1 + k1) % 26, (m2 + k2) % 26, ..., (mi + ki) % 26)
    D(m) = ((c1 - k1) % 26, (c2 - k2) % 26, ..., (ci - ki) % 26)

Like the other naive ciphers, this shouldn't be used. It is however the most
secure of the group.
"""
from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print 'Key: %s' % key
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted


if __name__ == '__main__':
    show_result('ihadadream', 'boom')
