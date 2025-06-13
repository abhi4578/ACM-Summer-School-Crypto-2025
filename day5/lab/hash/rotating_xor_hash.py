from hash_helper import rotl

def rotating_xor_hash(m):
    h=0
    for i in range(len(m)):
        h = rotl(h,5) ^ ord(m[i])
    return h

def main():
    msg = "Hello World"
    h = rotating_xor_hash(msg)
    print(h)

main()
