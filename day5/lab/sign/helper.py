import socket
import random

#------------------------------Globals------------------------------
inf = (1<<256)  # Serves as infinity for modular arithmetic
is_prime = []
primes = []
#------------------------------------------------------------------
#--------------------------Helper Functions------------------------
# L function for Paillier
def L(x,n):
    return (x - 1) // n
#------------------------------------------------------------------
def sieve_of_eratosthenes(bound):
    global is_prime, primes
    if(len(primes) > 0):
        return
    is_prime = [True] * (bound + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(bound + 1):
        if(is_prime[i] == False):
            continue
        primes.append(i)
        for j in range(i * i, bound + 1, i):
            is_prime[j] = False
#------------------------------------------------------------------
def weak_prime_test(n):
    global primes
    for i in range(len(primes)):
        if(primes[i] * primes[i] > n):
            break
        if(n % primes[i] == 0):
            return False
    return True
#----------------------------------------------------------------
# A composite number passes with probability 4^{-k}
def miller_rabin(n, k):                       # Strong Prime Test
    d = n - 1
    s = 0   
    while(d % 2 == 0):
        d //= 2
        s += 1
    for _ in range(k):
        a = random.SystemRandom().randint(2, n - 2)
        x = mod_exp(a, d, n)
        for _ in range(s):
            y = mod_exp(x, 2, n)
            if(y == 1 and x != 1 and x != n - 1):
                return False
            x = y
        if(y != 1):
            return False
    return True
#------------------------------------------------------------------
# Standard way of generating very large primes
def gen_large_prime(bit_length):
    lower = mod_exp(2, bit_length - 1, inf)
    upper = mod_exp(2, bit_length, inf)
    while(True):
        n = random.SystemRandom().randint(lower, upper)
        if(weak_prime_test(n) and miller_rabin(n, 20)):
            return n
#------------------------------------------------------------------
def mod_exp(k, e, N):
	if(e == 0):
		return 1
	ans = mod_exp(k, e//2, N)%N
	ans = (ans * ans)%N
	if(e%2 == 1):
		ans = (ans * k)%N
	return ans
#----------------------------------------------------------------
def socket_setup(port = 12567, client = False):
    s = socket.socket()         
    port = port  
    if(client):
        try:
            s.connect(('127.0.0.1', port))
        except Exception as e:
            print("Connection Failed: ", e)
            s.close()
            exit()
    else:
        s.bind(('', port))
        s.listen(5)
    return s
#----------------------------------------------------------------
def gcd(a,b):
    if(b == 0):
        return a
    return gcd(b, a%b)
#----------------------------------------------------------------
def extended_gcd(a, b):
	if(b == 0):
		return (a, 1, 0)
	d, x_1, y_1 = extended_gcd(b, a%b)
	return(d, y_1, x_1 - y_1*(a // b))
#----------------------------------------------------------------
def mod_inverse(a, b):
	d, x, y = extended_gcd(a,b)
	if(d!=1):
		print(f"{a}, {b} have gcd {d} > 1, hence inverse does not exist")
		return
	return x%b
#----------------------------------------------------------------
# Just converts a string to its binary and then to its 
# integer representation
def encode_message(message):
    return int.from_bytes(message.encode("ascii"), "big")
#----------------------------------------------------------------   
def decode_message(encoded_num: int) -> str:
    try:
        byte_length = (encoded_num.bit_length() + 7) // 8
        return encoded_num.to_bytes(byte_length, 'big').decode('ascii')
    except (ValueError, UnicodeDecodeError) as e:
        print(f"Error decoding number {encoded_num}: {e}")
        return None
#-------------------------Populate primes[]----------------------
sieve_of_eratosthenes(10000)
#----------------------------------------------------------------