"""
Substitution Cipher

The substitution cipher is one in which one value maps to another value to
form a table. For instance:

    A == F
    B == Z
    ...

This cipher is not secure as once the pairs are found out, any other
ciphertext may be decrypted with ease. To crack it, most commonly letter
frequencies are used.

While we can make it harder to crack by using special characters, upper and
lower case letters, and numbers, it still doesn't mean that it's a hard cipher
to crack.
"""
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)


def show_result(plaintext):
    """Generate a resulting cipher with elements shown"""
    key = generate_key()
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print 'Key: %s' % key
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted


if __name__ == '__main__':
    show_result('Hello, world!')
