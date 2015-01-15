"""
Caesar Cipher

The caesar cipher is a symmetric key cipher that operates on the premise that
you rotate the alphabet a set number of characters creating a key. For
instance:

    A == Z
    B == A
    C == B
    ...
    Z == Y

The cipher is very insecure as when you find the offset you have found the
key. Running it through 26 variations will crack it easily. It also can be
cracked by letter frequencies.

It was secure most likely when Julius Caesar invented it but never again.

One way to encrypt/decrypt the letters is:
    E(x) = (x + n) % 26
    D(x) = (x - n) % 26

The rot13 algorithm is a common occurrence of the Caesar cipher with a 13
rotation.
"""
key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


def show_result(plaintext, n):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(n, plaintext)
    decrypted = decrypt(n, encrypted)

    print 'Rotation: %s' % n
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted


if __name__ == '__main__':
    show_result('the grass is always greener', 5)
