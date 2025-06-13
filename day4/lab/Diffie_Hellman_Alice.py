
from helper import *
import random
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#-----------------------------------------------------------------------------
#--------------------------------Client Setup---------------------------------

def Alice(logging = False):
    c = socket_setup(client = True)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False): 
        group_sz = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Group Size Established to be ", group_sz)
            print("PUBLIC: Generator g = 2")
        # Generator 2
        g=2
        #------------------------------
        # a is the private key of Alice
        a = random.SystemRandom().randint(1, group_sz - 1)
        
        # EXERCISE: Find g^a and uncomment the following lines
        g_a = pow(g,a,group_sz)
        if(logging):
            print("PUBLIC: Sending g^a = ", g_a)
        c.send(f"{g_a}".encode())
        #------------------------------
        g_b = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Received g^b = ", g_b)
        #------------------------------
        # EXERCISE: Find g^ab and uncomment the following lines
        g_ab = pow(g_b, a, group_sz)
        if(logging):
             print("PRIVATE: Constructed g^ab = ", g_ab)
             print("---Key Exchange Complete---")

        #------------------------------
        # Now you can use your shared key to encrypt and send messages to Bob

        msg = b"Type your message here"
        aes = AESGCM(g_ab.to_bytes(16, 'big'))
        nonce = os.urandom(12)
        ciphertext = aes.encrypt(nonce, msg, None)
        c.send(nonce + ciphertext)
        if(logging):
            print("Sent ciphertext: ", ciphertext)
        c.close()
        #------------------------------ 
        # return a, g_a, g_ab
        
    return interaction(logging)

#----------------------------------------------------------------
Alice(logging = True)
