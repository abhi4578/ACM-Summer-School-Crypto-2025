from hash_helper import *

def additive_hash(m):
    h = 0
    # Fill in the code here
    for i in m:
        h+=ord(i)
    h = h%2**32
    return h
def preimage_attack_additive_hash(h):
    m=''
    while h > 0:
        m+= chr(min(ord('Z'), h))
        h-=min(ord('Z'), h)
    return m
def main():
    msg = "Hello World!"
    h = additive_hash(msg)
    print(h)
    preimage_attack(additive_hash,h)
    

main()


