from helper import *
from hashlib import sha256

bit_length = 128
m = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Signed by Alice"

def Alice_Hash_Sign(m, logging = False):
    c = socket_setup(client = True)
    #-------------------------------
    # EXERCISE: Generate public private key pair of RSA. Copy answer from previous exercise.
    p = gen_large_prime(128)
    q = gen_large_prime(128)
    n = p*q
    totient = (p-1)*(q-1)
    e = 65537
    d = pow(e,-1,totient)
    #-------------------------------
    # Split message into blocks of 16 characters
    # EXERCISE: Break message into blocks of 16 characters
    blocks =  []
    
    if len(m) % 16 !=0:
        padded_m = m + '0'*(16- len(m)%16)

    for i in range(0,len(m),16):
        blocks.append(padded_m[i:i+16])
    
    print("Message: ", m)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False): 
        bob_pub_key_str = c.recv(1024).decode()
        n_, e_ = map(int, bob_pub_key_str.split(","))
        if(logging):
            print("Bob's Public Key Received: ", bob_pub_key_str)
        #--------------------------------
        # Uncomment the below after getting private and public keys
        c.send(f"{n}, {e}".encode())
        if(logging):
            print("Alice's Public Key Sent: ", f"{n}, {e}")
        #--------------------------------
        # EXERCISE: Encrypt each block and send
        cipher_text =''
        for m_ in blocks:
            cipher_text += str(pow(encode_message(m_),e_,n_)) + ','
        c.send(cipher_text.encode())
        
        #------------------------------
        
        # Send -1 to indicate end of blocks
        c.send(f"-1,".encode())
        #--------------------------------
        # Find hash value of full message
        # sign and send it
        sha256().update(str(m).encode())
        hash_m = int(sha256().hexdigest(), 16)
        #--------------------------------
        # EXERCISE: Compute signature and send it
        signature = pow(hash_m, d, n)
        c.send(f"{signature}".encode())
        #--------------------------------
    interaction(logging)
    #----------------------------------------------------------------
Alice_Hash_Sign(m, logging = True)