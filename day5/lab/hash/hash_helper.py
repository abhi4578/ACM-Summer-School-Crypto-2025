import itertools

MASK32 = 0xFFFFFFFF
MASK64 = 0xFFFFFFFFFFFFFFFF

def rotl(x, r, bit = 32):
    MASK = MASK32 if bit == 32 else MASK64
    y = x & MASK
    for _ in range(r):
        b = (y & ( 1 << (bit - 1))) >> (bit - 1)
        y = y << 1
        y |= b
        y &= MASK
    return y

def preimage_attack(H, hash_value, max_len = 20, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    cnt = 0
    for n in range(max_len):
        for chars in itertools.product(alphabet, repeat=n):
            m = "".join(chars)
            cnt += 1
            if H(m) == hash_value:
                return m, cnt
    return None, cnt


