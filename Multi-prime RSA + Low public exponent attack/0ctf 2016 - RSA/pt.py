#!usr/bin/env python
#-*- coding:utf-8 -*-

import gmpy2

f = open('flag.enc','r').read()

ciphertext = int(f.encode('hex'),16)

print int(f.encode('hex'),16)

p = 26440615366395242196516853423447

q = 27038194053540661979045656526063

r = 32581479300404876772405716877547

print gmpy2.invert(ciphertext,p)
print gmpy2.invert(ciphertext,q)
print gmpy2.invert(ciphertext,r)
