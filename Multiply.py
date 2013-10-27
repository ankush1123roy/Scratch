import time
def naive(a,b):
    x = a 
    y = b 
    z = 0 
    while x > 0:
        z = z + y 
        x -= 1
    return z

def russian(a,b):
    x = a
    y = b 
    z = 0 
    while x > 0:
        if x % 2 == 1: z = z + y
        x = x >> 1
        y = y << 1
    return z
a = time.time()
K = naive(100000000,10000)
b = time.time()
K1 = russian(200000000,10000)
c = time.time()
print K, b-a
print K1, c-b
