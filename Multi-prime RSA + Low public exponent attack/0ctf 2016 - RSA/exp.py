from Crypto.Util.number import *

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def gauss(c0, c1, c2, n0, n1, n2):
    N = n0 * n1 * n2
    N0 = N / n0
    N1 = N / n1
    N2 = N / n2
    d0 = modinv(N0, n0)
    d1 = modinv(N1, n1)
    d2 = modinv(N2, n2)
    return (c0*N0*d0 + c1*N1*d1 + c2*N2*d2) % N

roots0 = [5686385026105901867473638678946, 7379361747422713811654086477766, 13374868592866626517389128266735]
roots1 = [19616973567618515464515107624812]
roots2 = [6149264605288583791069539134541, 13028011585706956936052628027629, 13404203109409336045283549715377]
p = 26440615366395242196516853423447

q = 27038194053540661979045656526063

r = 32581479300404876772405716877547

for r0 in roots0:
    for r1 in roots1:
        for r2 in roots2:
            M = gauss(r0, r1, r2, p, q, r)
            print long_to_bytes(M)
