'''
Write the following three functions by using python. When you submit, you should submit a report file (modexp.pdf) and a souce file (modexp.py).
The report file should contain a source code and the running results of your functions in the python shell.
The python source file should contain the souce code of your functions.

1) mod_exp(a, e, n): it returns a^e mod n.
2) crt(p, q, a, b): it returns the value x that satisfies x = a mod p and x = b mod q where p and q are primes.
3) crt_list(primes, values): it returns the value x that satisfies x = values[i] mod primes[i] for all i in the list.

The report should contain the results of the following examples:

a) mod_exp(3, 12345, 97)
b) mod_exp(3, 123456789012345, 976)
c) crt(10, 21, 1, 2)
d) crt(257, 293, 11, 13)
e) crt_list([10, 21, 29], [1, 2, 3]) 
f) crt_list([257, 293, 337], [11, 13, 31])
'''

def mod_exp(a,e,n) :
    r = 1
    bb = bin(e)[2:]
    print(bb)
    for bit in range(len(bb)) :
        r = (r*r)%n
        if int(bb[bit]) == 1 :
            r = r*a%n
    return r

def modexp_lr(a, b, n):
    r = 1
    print(bits_of_n(b))
    for bit in reversed(bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    print (r)



def crt(p,q,a,b) :
    N = p * q
    n_1,n_2 = N//p,N//q
    sum_ = a*multi_inverse(n_1,p)*n_1 + b *multi_inverse(n_2, q) *n_2
    return sum_%N

def crt_list(n,a) :
    sum_ = 0
    N = 1
    for i in n :
        N *= i
    for i,j in zip(n,a) :
        p = N // i
        sum_ += j * multi_inverse (p,i) *p
    return sum_ % N 

def multi_inverse(p,n_i) :
    N = n_i
    s,t = 0,1
    if n_i == 1 :
        return 1
    while p > 1 :
        q = p // n_i
        p,n_i = n_i, p%n_i
        s,t = t - q*s, s
    if t < 0 :
        t = t+N
    return t

print("mod_exp(3,12345,97) : ",mod_exp(3,12345,97))
print("mod_exp(3, 123456789012345, 976) :",mod_exp(3, 123456789012345, 976))
print("crt(10, 21, 1, 2) :",crt(10, 21, 1, 2))
print("crt(257, 293, 11, 13) :",crt(257, 293, 11, 13))
print("crt_list([10, 21, 29], [1, 2, 3]) :",crt_list([10, 21, 29], [1, 2, 3]))
print("crt_list([257, 293, 337], [11, 13, 31]) :",crt_list([257, 293, 337], [11, 13, 31]))


