import random

def find_two(n) :
    i = 0
    m = n-1
    while m%2 == 0 :
        i = i+1
        m //= 2
    return i, int(m)

def miller_rabin_test(n,b,s,t) :
    a = pow(b,t,n)
    for i in range(0,s) :
        if a == 1 or a == n-1:
            return a
        a = pow(a,2,n)  
    return 0

def is_prime(n) :
    s,t = find_two(n)
    for i in range(400) :
        b = random.randint(2,n-1)
        c = miller_rabin_test(n,b,s,t)
        if c == 0:
            print("Result : Composite")
            return 0
    print("Result : Can be prime!!")

print("a) is_prime(561)")
is_prime(561)
print("b) is_prime(569)")
is_prime(569)
print("c) is_prime(2 ** (2 ** 4) + 1)")
is_prime(2 ** (2 ** 4) + 1)
print("d) is_prime(2 ** (2 ** 10) + 1)")
is_prime(2 ** (2 ** 10) + 1)
print("e) is_prime(2 ** 1279 - 1)")
is_prime(2 ** 1279 - 1)
print("f) is_prime(2 ** 2203 - 1)")
is_prime(2 ** 2203 - 1)
print("g) is_prime(2 ** 3217 - 1)")
is_prime(2 ** 3217 - 1)
