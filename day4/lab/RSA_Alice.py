from helper import *

m = "RSA Works! Hello Bob!"

def Alice(m, logging = False):
    c = socket_setup(client = True)
    
    encoded_m = encode_message(m)
    print("Message: ", m)
    print("Encoded Message: ", encoded_m)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False): 
        pub_key_str = c.recv(1024).decode()
        n, e = map(int, pub_key_str.split(","))
        if(logging):
            print("Public Key Received: ", pub_key_str)
        #------------------------------
        # EXERCISE: Find cipher_text and uncomment the following lines
        cipher_text = pow(encoded_m,e,n)
        c.send(f"{cipher_text}".encode())
        if(logging):
            print("Cipher text Sent: ", cipher_text)
    interaction(logging)
    #----------------------------------------------------------------
Alice(m, logging = True)