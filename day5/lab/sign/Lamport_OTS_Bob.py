from helper import socket_setup
from signature_helper import *
import os
import json
from random import SystemRandom
from hashlib import sha256


msg = "Hello, World!"

def Bob(m, logging = False):
    s = socket_setup()
    rng = SystemRandom()
    #-------------------------------
    # EXERCISE: Generate private and public keys
    # priv_key = 
    # pub_key = 
    #-------------------------------
    def interaction(logging = False):
        c, addr = s.accept()
        if(logging):
            print("Connection established")
        # Uncomment the following after getting private and public keys
        # for p0, p1 in pub_key:
        #     send_bytes(c, p0)
        #     send_bytes(c, p1)
        if(logging):
            print("Sent public key")
        #-------------------------------
        send_string(c, m)
        if(logging):
            print("Sent message: ", m)
        #-------------------------------
        # EXERCISE: Compute the hash and the signature and send it
        # Uncomment the following after having done it
        # send_json(c, signature)
        # if(logging):
        #     print("Sent signature: ", signature)
        #-------------------------------
        c.close()
        return signature
    return interaction(logging)
#-------------------------------
Bob(msg, logging = True)