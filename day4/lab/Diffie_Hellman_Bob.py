from helper import *
import random
from cryptography.hazmat.primitives.ciphers.aead import AESGCM



#----------------------------------------------------------------
#--------------------Server Setup--------------------------------
def Bob(logging = False):
    s = socket_setup()
    # EXERCISE: Find a large prime for the group size
    group_sz = gen_large_prime(128)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False):
        c, addr = s.accept()

        if(logging):
            print("PUBLIC: Connection Established. Establishing Group Size.")
        # Uncomment after finding group_sz
        c.send(f"{group_sz}".encode())
        
        if(logging):
            print("PUBLIC: Group Size Established to be ", group_sz)
            print("PUBLIC: Generator g = 2")
        #------------------------------
        #EXERCISE: Write the missing code, import necessary functions from helper.py
        #------------------------------
        # Generator 2
        g=2
        g_a = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Received g^a = ", g_a)
        # b is the private key of Alice
        b = random.SystemRandom().randint(1, group_sz - 1)
        g_b = pow(g,b,group_sz)
        if(logging):
            print("PUBLIC: Sending g^b = ", g_b)
        c.send(f"{g_b}".encode())
        g_ab = pow(g_a, b, group_sz)
        if(logging):
             print("PRIVATE: Constructed g^ab = ", g_ab)
             print("---Key Exchange Complete---")
        #------------------------------ 
        # Receiving ciphertext from Alice
        aes = AESGCM(g_ab.to_bytes(16, 'big'))
        data = c.recv(1024)
        nonce, ciphertext = data[:12], data[12:]
        if(logging):
            print("Received ciphertext: ", data)
        plaintext = aes.decrypt(nonce, ciphertext, None)
        if(logging):
            print("Plaintext: ", plaintext.decode())
        # ------------------------------
        # BONUS: Send a message back to Alice
        s.close()
        # return b, g_b, g_ab
    return interaction(logging)
#----------------------------------------------------------------
Bob(logging = True)

# EXERCISE: Add an extra interaction to establish generator g instead of fixing it as 2