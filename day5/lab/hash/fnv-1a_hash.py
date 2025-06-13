# Fowler–Noll–Vo hash function
# Named after the creators, Glenn Fowler, Landon Curt Noll, and Kiem-Phong Vo

# Used for simplicity and efficiency, has rare collisions and good distribution
# Was used in Python's hash() function until Python 3.4
def fnv1a(m):
    fnv_prime = 0x1000193
    fnv_offset = 0x811c9dc5
    
    # Fill in the code here
    return 0


def main(): 
    msg = "Hello World"
    h = fnv1a(msg)
    print(h)

main()
