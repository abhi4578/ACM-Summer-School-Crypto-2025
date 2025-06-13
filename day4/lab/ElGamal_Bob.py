from helper import *
import random

#----------------------------------------------------------------
def Bob(logging = False):
    _s = socket_setup()
    c, addr = _s.accept()
    #----------------------------------------------------------------

    G_sz = gen_large_prime(128)
    g, x = 2, random.SystemRandom().randint(1, G_sz - 1)
    h = mod_exp(g, x, G_sz)
    pub_key_str = f"{G_sz},{g},{h}"
    
    #----------------------------------------------------------------
    def interaction(logging = False):   
        if(logging):
            print("Connection Established. Sending public key.")
        c.send(pub_key_str.encode())
        if(logging):
            print("Public Key Sent: ", pub_key_str)
        #------------------------------
        cipher_str = c.recv(1024).decode()
        c1, c2 = map(int, cipher_str.split(","))

        if(logging):
            print("Cipher text Received: ", cipher_str)
        c.close()
        #------------------------------
        s = mod_exp(c1, x, G_sz)
        #------------------------------
        encoded_m = (c2 * mod_inverse(s, G_sz)) % G_sz 
        # EXERCISE: Find a faster way of inverting s
        # Hint: What do we know about G_sz?
        m = decode_message(encoded_m)
        return m
    #----------------------------------------------------------------
    m = interaction(logging)
    print("Decrypted Message: ", m)
#----------------------------------------------------------------

Bob(logging = True) 