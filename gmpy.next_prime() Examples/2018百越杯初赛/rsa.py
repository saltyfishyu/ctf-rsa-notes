#!/usr/bin/env python3
import gmpy2
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode


flag = open('flag', 'r').read().strip() * 23


def encrypt(p, q, e, msg):
    while True:
        n = p * q
        try:
            phi = (p - 1)*(q - 1)
            pubkey = RSA.construct((int(n), int(e)))
            key = PKCS1_v1_5.new(pubkey)
            enc = b64encode(key.encrypt(msg))
            return enc
        except:
            p = gmpy2.next_prime(p**2 + q**2)
            q = gmpy2.next_prime(2*p*q)
            e = gmpy2.next_prime(e**2)


p = getPrime(128)
q = getPrime(128)
n = p*q
e = getPrime(64)
pubkey = RSA.construct((n, e))
with open('pubkey.pem', 'wb') as f:
    f.write(pubkey.exportKey())
with open('flag.enc', 'wb') as g:
    g.write(encrypt(p, q, e, flag.encode()))
