from helper import *
from hashlib import sha256

bit_length = 128

def Bob_Hash_Verify(logging = False):
    s = socket_setup()
    #-------------------------------
    # EXERCISE: Generate public private key pair of RSA. Copy answer from previous exercise.
    p = gen_large_prime(128)
    q = gen_large_prime(128)
    n = p*q
    totient = (p-1)*(q-1)
    e = 65537
    d = pow(e,-1,totient)
    #-------------------------------
    # Uncomment the below after getting private and public keys
    def interaction(logging = False):
        c, addr = s.accept()
        pubkey_str = f"{n}, {e}"
        if(logging):
            print("Connection established. Sending Bob's public key: ", pubkey_str)
        c.send(pubkey_str.encode())
        (n_, e_) = map(int, c.recv(1024).decode().split(","))
        if(logging):
            print("Alice's public key received: ", f"{n_}, {e_}")
        #----------------------------------------------------------------

        # We want to receive the message in chunks, however,
        # due to message coalescing, TCP might bundle multiple messages
        # into one packet. This is a result of Nagle's algorithm.
        # To handle this, we maintain a buffer and extract cipher texts
        # from the buffer until we encounter a -1, which indicates end of 
        # cipher text stream. The next message is the signature on the full 
        # message. We then verify the signature against the hash of the full 
        # message.
        
        #----------------------------------------------------------------
        buffer, m, flag = "", "", True
        while(flag):
            data = c.recv(1024).decode()
            buffer += data
            while "," in buffer:
                cipher_text, buffer = buffer.split(",", 1)
                cipher_text = int(cipher_text)
                if(cipher_text == -1):
                    flag = False
                    break
                if(logging):
                    print("Cipher Text: ", cipher_text)
                #----------------------------------------------------------------
                # EXERCISE: Decrypt and decode the cipher text to get a block of
                dec_= decode_message(mod_exp(cipher_text, d, n))
                m_ = dec_.strip('0')
                m += m_
                #----------------------------------------------------------------
        #----------------------------------------------------------------
        if(buffer != ""):
            # Handle the case where signature was already received and stored in buffer
            signature = int(buffer)
        else:
            # Else receive it over the socket
            signature = int(c.recv(1024).decode())
        #----------------------------------------------------------------
        # EXERCISE: Compute signature and verify its authenticity
        # Uncomment the remaining when done
        sha256().update(str(m).encode())
        signature_ = int(sha256().hexdigest(), 16) % n_
        signature = pow(signature, e_, n_)
        if(signature != signature_):
            print("!!!Signature Verification Failed!!!")
        else:
            print("---Signature Verification Passed---")
        return m
    #-------------------------------    
    m = interaction(logging)
    print("Decrypted message: ", m)
#----------------------------------------------------------------
Bob_Hash_Verify(logging = True)