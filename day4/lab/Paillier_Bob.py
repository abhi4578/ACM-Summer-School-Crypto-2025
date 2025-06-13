from helper import *

bit_length = 128

def Bob(logging = False):   
    s = socket_setup()
    #-------------------------------
    # Generating two large primes p and q
    p = gen_large_prime(bit_length)
    q = gen_large_prime(bit_length)
    if(gcd(p * q, (p - 1) * (q - 1)) != 1):
        print("p and q are not of same length, check `gen_large_prime`")
        exit()
    # EXERCISE: Generate public and private keys and uncomment the subsequent lines
    # Public Key
    # n = 
    # g = 
    # Private Key
    # _lambda = 
    # mu = 
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False):
        c, addr = s.accept()
        # pubkey_str = f"{n},{g}"
        # if(logging):
        #     print("Connection established. Sending public key: ", pubkey_str)
        #------------------------------
        # c.send(pubkey_str.encode())
        cipher_text = int(c.recv(1024).decode())
        if(logging):
            print("Received cipher text: ", cipher_text)
        #------------------------------
        # EXERCISE: Decrypt the ciphertext
        # encoded_m = 
        # return decode_message(encoded_m)
        #------------------------------
    m = interaction(logging)
    print("Decrypted message: ", m)
    #----------------------------------------------------------------
Bob(logging = True)