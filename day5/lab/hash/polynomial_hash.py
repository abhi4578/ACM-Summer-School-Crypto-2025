def polynomial_hash(m):
    h = 0
    p = 53
    M = 10 ** 9 + p
    for i in range(len(m)):
        h+=(ord(m[i]) * p ** i) % M
    return h


msg = "Hello World"
h = polynomial_hash(msg)
print(h)
