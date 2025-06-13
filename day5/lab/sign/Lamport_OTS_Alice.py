from helper import *
from signature_helper import *
import json
from hashlib import sha256

def Alice(logging = False):
    s = socket_setup(client = True)
    #-------------------------------
    def interaction(logging = False):
        pub_key = [(recv_bytes(s), recv_bytes(s)) for _ in range(256)]
        if(logging):
            print("Received public key: ", pub_key)
        #-------------------------------
        m = recv_string(s)
        if(logging):
            print("Received message: ", m)
        
        #-------------------------------
        signature = recv_json(s)
        if(logging):
            print("Received signature: ", signature)
        #-------------------------------
        # EXERCISE: Verify the signature and return 0/1
        s.close()
        # return 1
    b = interaction(logging)
    if(b):
        print("----SIGNATURE VERIFIED----")
    else:
        print("----SIGNATURE VERIFICATION FAILED----")
#-------------------------------
Alice(logging = True)