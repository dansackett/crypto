# Crypto Terminology

The following terms are common in the world of Cryptography.

## Basics

**Handshake Protocol:** The idea of a handshake between parties uses a key on
both sides. When one side requests data from the other, they check the keys
and if allowed they make the exchange. This is best seen with public and
private keys between entities.

**Symmetric Encryption System (Symmetric Ciphers):** A system that implements
both an encryption and a decryption algorithm with a shared secret key. This
is such that:

```
ciphertext = E(k, m)
plaintext  = D(k, E(k, m))
```

**Uniform Distribution:** The theorem that says that a finite number of values
are likely to occur with equal probability 1/n. Essentially, a known number of
outcomes equally likely to happen.

**Event:** In a uniform distribution, a single instance occuring can be
considered an event.

**Union Bound:** The probability that one event or another will happen.

**Random Variable:** A variable in which the least significant bit has the
same probability of occuring as another in the space {0,1}^n

**Independence:** Two events A and B are independent if one event happens and
doesn't tell use anything about the other.

**XOR:** "Exclusive Or" or an operator in which given two values A and B, we
return true if and only if we have one or the other, not both. This can be
seen in a truth table:

```
INPUT  |  OUTPUT
----------------
0   0  |    0
0   1  |    1
1   0  |    1
1   1  |    0
```

## Ciphers

**Substitution Cipher:** A cipher which creates a mapping between keys and
randomized keys as values.

**Caesar Cipher:** A shift by n cipher which rotates an alphabet of characters
to create a new mapping.

**Vigenere Cipher:** A chain of Caesar Ciphers with a repeating key for the
length of the message.
