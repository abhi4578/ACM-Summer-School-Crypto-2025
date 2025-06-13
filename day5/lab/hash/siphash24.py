from hash_helper import rotl, MASK64
import os 

# Add-Rotate-XOR family of PRFs designed created by Jean-Philippe Aumasson
# and Daniel J. Bernstein
# Designed as response to 2011 HashDoS attacks
# Used in Python's hash() function

def siphash24(m, key):
    b = m.encode()
    assert(len(key) == 16)

    k0 = int.from_bytes(key[:8], 'little')
    k1 = int.from_bytes(key[8:], 'little')

    # Constants. If split into bytes, in big-endian order,
    # their corresponding ascii characters spell something interesting

    c1 = 0x736f6d6570736575
    c2 = 0x646f72616e646f6d
    c3 = 0x6c7967656e657261
    c4 = 0x7465646279746573

    # Can verify by uncommenting the following code
    # for val in {c1, c2, c3, c4}:
    #     b = val.to_bytes(8, 'big')
    #     hex_bytes = [f"0x{x:02x}" for x in b]
    #     ascii_str = b.decode('ascii')
    #     print(f"{val}: bytes={hex_bytes} -> ascii='{ascii_str}'")

    # EXERCISE: Find v0, v1, v2, v3
    v0 = 0
    v1 = 0
    v2 = 0
    v3 = 0

    # EXERCISE: Implement the SipHash rounds
    def sip_round():
        nonlocal v0, v1, v2, v3
        return
    
    # Find the number of full blocks
    end = (len(b) // 8) * 8

    # Process each full block
    # Interpret as a little endian integer and do SIP rounds
    for i in range(0, end, 8):
        block = int.from_bytes(b[i:i+8], 'little')
        v3 ^= block
        sip_round(); sip_round()
        v0 ^= block

    # Process the last block
    rem = b[end:]
    # Pad with 0s to make it full 8 bytes
    last_block = int.from_bytes(rem + b'\x00' * (8 - len(rem)), 'little')
    # Add the length of the message to the first byte of the last block
    last_block |= (len(b) & 0xff) << 56
    # XOR the last block with v3 and do SIP rounds
    v3 ^= last_block
    sip_round(); sip_round()
    v0 ^= last_block

    # More SIP rounds
    v2 ^= 0xff
    for _ in range(4):
        sip_round()

    # XOR and mod 2^64
    return (v0 ^ v1 ^ v2 ^ v3) & MASK64


def main():
    msg = "Hello World"
    key = os.urandom(16)
    h = siphash24(msg, key)
    print(f"Message: {msg}")
    print(f"Key: {key}")
    print(f"Hashed message: {h}")

main()