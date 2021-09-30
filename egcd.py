'''
a) extended_gcd(45, 78)
b) extended_gcd(666, 1428)
c) extended_gcd(1020, 10290)
d) extended_gcd(2 ** 20 + 4, 3 ** 10 + 5)
e) extended_gcd(2 ** 30 + 1, 3 ** 30 + 6)
'''

def gcd(x,y) :
    while(y) :
        x,y = y,x%y
    return x

def extended_gcd(a,b) :
    x0, x1, y0,y1 = 0,1,1,0
    x,y = a,b
    while a != 0:
        q,b,a = b//a, a, b%a
        y0, y1 = y1, y0-q*y1
        x0, x1 = x1, x0 -q*x1

    print("%d*%d + %d*%d = %d" %(x0,x, y0,y, b))


extended_gcd(45,78)
extended_gcd(666,1428)
extended_gcd(1020,10290)
extended_gcd(2 ** 20 + 4, 3 ** 10 +5)
extended_gcd(2 ** 30 + 1, 3 ** 30 + 6)
