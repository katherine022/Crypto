import random

def gcd(x,y) :
    while(y) :
        x,y = y,x%y
    return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x%m

def mod_exp(a,e,n) :
    r = 1
    bb = bin(e)[2:]
    for bit in range(len(bb)) :
        r = (r*r)%n
        if int(bb[bit]) == 1 :
            r = r*a%n
    return r

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
    if n == 2 :
        return 1
    if n < 2 or n%2 == 0:
        return 0
    s,t = find_two(n)
    for i in range(20) :
        b = random.randint(2,n-1)
        c = miller_rabin_test(n,b,s,t)
        if c == 0:
            return 0 ## 합성수
    return 1 ##소수 

def primes(length) :
    while 1 :
        p = random.randrange(pow(2,length-1), pow(2,length))
        if not is_prime(p) :
            continue
        else :
            break
    return p

def rsa_genkey(key_length) :
    p_length = key_length // 2

    q_length = key_length - p_length

    while 1 :
        p = primes(p_length)
        q = primes(q_length)
        if p != q :
            break

    N = p * q
    pie_n = (p-1)*(q-1)

    e = 65537
    d = modinv(e,pie_n)

    public_key = [N,e]
    secret_key = [p,q,d]

    return public_key, secret_key

def rsa_encrypt(m,pk) :
    CT = mod_exp(m,pk[1], pk[0])
    return CT

def rsa_decrypt(ct,sk) :
    PT = mod_exp(ct, sk[2], sk[0]*sk[1])
    return PT

#####key_length가 1024일때
print("Key Length = 1024")
pk,sk = rsa_genkey(1024)
#print("Secret key :",sk,"\n", "Public key :", pk)
print("First Message : 1234")
m = 1234
ct = rsa_encrypt(m,pk)
print("CipherText : ", ct)
pt = rsa_decrypt(ct,sk)
print("PlainText :", pt)

print()
print("---------------------------------------------------------------------------------------------------------")
print()

###key_length가 512일때
print("Key Length = 512")
pk, sk = rsa_genkey(512)
print("First Message : 1234")
m = 1234
ct = rsa_encrypt(m,pk)
print("CipherText :",ct)
pt = rsa_decrypt(ct,sk)
print("PlainText :", pt)

print()
print("---------------------------------------------------------------------------------------------------------")
print()

###key_length가 256일때
print("Key Length = 256")
pk, sk = rsa_genkey(256)
print("First Message : 1234")
m = 1234
ct = rsa_encrypt(m,pk)
print("CipherText :",ct)
pt = rsa_decrypt(ct,sk)
print("PlainText :", pt)
