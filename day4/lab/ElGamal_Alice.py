from helper import *
import random

m = "ElGamal Works!"
#----------------------------------------------------------------
def Alice(m, logging = False):
    c = socket_setup(client = True)
    #----------------------------------------------------------------
    def interaction(logging = False):

        pub_key_str = c.recv(1024).decode()
        G_sz, g, h = map(int, pub_key_str.split(","))
        if(logging):
            print("Public Key Received: ", pub_key_str)

        #------------------------------
        # EXERCISE: Write the missing code, import necessary functions from helper.py
        encoded_m = encode_message(m)
        if(logging):
            print("M: ", encoded_m)

        #------------------------------

        # EXERCISE: Find y, s and cipher_text and uncomment the following lines
        y = random.SystemRandom().randint(1, G_sz - 1)
        s = mod_exp(h,y,G_sz)
        cipher_text = [ mod_exp(g, y, G_sz), pow(encoded_m,1,G_sz)*pow(s,1,G_sz)%G_sz]

        #------------------------------
        # Uncomment when above code is complete

        c.send(f"{cipher_text[0]},{cipher_text[1]}".encode())
        if(logging):
            print("Cipher text Sent: ", cipher_text)
            
    #----------------------------------------------------------------
    interaction(logging)
#----------------------------------------------------------------
Alice(m, logging = True)