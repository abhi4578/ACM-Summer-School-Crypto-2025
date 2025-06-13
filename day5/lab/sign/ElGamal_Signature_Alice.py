from helper import *
from signature_helper import *
from hashlib import shake_128
import random

def Alice(logging = False):
    _s = socket_setup(client = True)
    #-------------------------------
    def interaction(logging = False):
        p, g, y, N = recv_json(_s)
        if(logging):
            print("Received public key and parameters")
        #-------------------------------
        m = recv_string(_s)
        if(logging):
            print("Received message: ", m)
        #-------------------------------
        r, s = recv_json(_s)
        if(logging):
            print("Received signature: ", (r, s))
        #-------------------------------
        # EXERCISE: Verify the signature and return 0/1
    b = interaction(logging)
    if(b):
        print("----SIGNATURE VERIFIED----")
    else:
        print("----SIGNATURE VERIFICATION FAILED----")
#-------------------------------
Alice(logging = True)