from helper import *
from signature_helper import *
from hashlib import shake_128
import random

key_length = 128
msg = "Hello, World!"

def gen_safe_prime(bit_length):
    while(True):
        q = gen_large_prime(bit_length)
        p = 2 * q + 1
        if(miller_rabin(p, 20)):
            return p, q

def Bob(m, logging = False):
    _s = socket_setup()
    #-------------------------------
    N = key_length
    p, q = gen_safe_prime(N)
    g = 2
    #-------------------------------
    x = random.SystemRandom().randint(2, p - 2) # Priv key
    y = mod_exp(g, x, p) # Pub key
    #-------------------------------
    def interaction(logging = False):
        c, addr = _s.accept()
        if(logging):
            print("Connection established")
        #-------------------------------
        send_json(c, (p, g, y, N))
        if(logging):
            print("Sent public key and parameters")
        #-------------------------------
        send_string(c, msg)
        if(logging):
            print("Sent message: ", msg)
        #-------------------------------
        while(True):
            k = random.SystemRandom().randint(2, p - 2)
            while(gcd(k, p - 1) != 1):
                k = random.SystemRandom().randint(2, p - 2)
            r = mod_exp(g, k, p)
            hash_m = shake_128(m.encode()).digest(N//8)
            hash_int = int.from_bytes(hash_m, 'big')
            s = (hash_int - x * r) * mod_inverse(k, p - 1) % (p - 1)
            if(s != 0):
                break
        send_json(c, (r, s))
        if(logging):
            print("Sent signature: ", (r, s))
        #-------------------------------
        c.close()
        return (r, s)
    return interaction(logging)
#-------------------------------
Bob(msg, logging = True)