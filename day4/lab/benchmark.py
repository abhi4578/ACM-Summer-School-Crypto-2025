import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

#----------------------------------------------------------------
# Size Limitations:
# 1. RSA: 4096 bit key = 512 bytes
#    PCKS1_OAEP padding overhead: 44 bytes
#    Message size <= 512 - 44 = 468 bytes
# 2. AES: 256 bit key = 32 bytes
#    Message size : Virtually unlimited since block cipher

# Note: We can divide large message into chunks and encrypt each chunk
# under public key, as we did in RSA_Signature module,
# but this would be much slower as can be seen from benchmarks

#----------------------------------------------------------------
# Performance Test: 468 byte sized string
# EXERCISE : Try 8192 bit key, with its respective max message size
#----------------------------------------------------------------
string_size = 468
test_string = "a" * string_size

def benchmark_aes(test_string, key_size = 256):
    start_time = time.time()
    #------------------------------
    test_string_bytes = test_string.encode("utf-8")
    #------------------------------
    # Key Generation and Encryption
    key = get_random_bytes(key_size//8)
    cipher_aes = AES.new(key, AES.MODE_EAX)
    nonce = cipher_aes.nonce
    cipher_text, tag = cipher_aes.encrypt_and_digest(test_string_bytes)
    #------------------------------
    # Decryption
    cipher_aes = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_bytes = cipher_aes.decrypt_and_verify(cipher_text, tag)
    result = decrypted_bytes.decode("utf-8")
    #------------------------------
    # Correctness Check
    assert result == test_string
    #------------------------------
    end_time = time.time()
    print(f"Time taken for AES encryption and decryption with key size {key_size} bits: {end_time - start_time} seconds")
#----------------------------------------------------------------
def benchmark_rsa(test_string, key_size = 4096):
    start_time = time.time()
    #------------------------------
    test_string_bytes = test_string.encode("utf-8")
    key = RSA.generate(key_size)
    pub_key = key.publickey()
    priv_key = key  
    #------------------------------
    # Encrypt
    cipher_rsa = PKCS1_OAEP.new(pub_key)
    cipher_text = cipher_rsa.encrypt(test_string_bytes)
    #------------------------------
    # Decrypt
    cipher_rsa = PKCS1_OAEP.new(priv_key)
    bytes = cipher_rsa.decrypt(cipher_text)
    result = bytes.decode("utf-8")
    #------------------------------
    # Correctness Check
    assert result == test_string
    #------------------------------
    end_time = time.time()
    print(f"Time taken for RSA encryption and decryption with key size {key_size} bits: {end_time - start_time} seconds")
#----------------------------------------------------------------
benchmark_aes(test_string)
benchmark_rsa(test_string)