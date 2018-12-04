from functools import reduce
from math import sqrt
from Crypto.Util.number import *

def next_prime(n):
    num = n + 1
    while True:
        if isPrime(num):
            return num
        num += 1
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m 

def bin_srch(target, lo, hi, f):
    if lo >= hi:
        return lo

    mid = (lo+hi)//2
    if f(mid) > target:
        return bin_srch(target, lo, mid-1, f)
    else:
        return bin_srch(target, mid+1, hi, f)

def poly(p):
    return 1000000 * pow(p, 4)

n = 603040899191765499692105412408128039799635285914243838639458755491385487537245112353139626673905393100145421529413079339538777058510964724244525164265239307111938912323072543529589488452173312928447289267651249034509309453696972053651162310797873759227949341560295688041964008368596191262760564685226946006231
c = 153348390614662968396805701018941225929976855876673665545678808357493865670852637784454103632206407687489178974011663144922612614936251484669376715328818177626125051048699207156003563901638883835345344061093282392322541967439067639713967480376436913225761668591305793224841429397848597912616509823391639856132

guess = bin_srch(n, 1<<251, 1<<252, poly)

p = 0
for g in range(-1000+guess, 1000+guess):
    if n % g == 0:
        p = g
        break

primes = [p]
for i in range(3):
    primes.append(next_prime(primes[i]*10))

print 'primes:', primes

phi = reduce(lambda a,b: a*(b-1), primes, 1)
print(long_to_bytes(pow(c, modinv(65537, phi), n)).decode('utf-8'))
