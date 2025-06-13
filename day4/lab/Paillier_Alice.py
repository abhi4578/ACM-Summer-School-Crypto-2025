from helper import *
import os

m = "Paillier Works!"

def Alice(m, logging = False):
    c = socket_setup(client = True)
    encoded_m = encode_message(m)
    if(logging):
        print("Message: ", m)
    #----------------------------------------------------------------
    def interaction(logging = False):
        pub_key_str = c.recv(1024).decode()
        n, g = map(int, pub_key_str.split(","))
        if(logging):
            print("Public Key Received: ", pub_key_str)
        #------------------------------
        # Generating 0 < r < n randomly such that gcd(r, n) = 1
        r = 0
        while(gcd(r, n) != 1):
            r = (int.from_bytes(os.urandom(128), "big") % (n-1)) + 1
        #------------------------------
        # EXERCISE: Encrypt the message and uncomment the following lines
        # cipher_text = 
        # c.send(f"{cipher_text}".encode())
        # if(logging):
        #     print("Cipher text Sent: ", cipher_text)
        c.close()
        #------------------------------
    interaction(logging)
    #----------------------------------------------------------------
    return encoded_m
Alice(m, logging = True)