import gmpy2
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def decrypt_RSA(cipherfile):
    n = 62078208638445817213739226854534031566665495569130972218813975279479576033261
    e = 9850747023606211927
    p = 336771668019607304680919844592337860739
    q = 184333227921154992916659782580114145999
    cipher = open(cipherfile, "r").read()
    while True:
        try:
            # key = open(privkey, "r").read()
            phi = (p - 1)*(q - 1)
            d = gmpy2.invert(e, phi)
            # pubkey = RSA.construct((long(n), long(e)))

            privkey = RSA.construct((long(n), long(e), long(d)))
            key = PKCS1_v1_5.new(privkey)
            decrypted = key.decrypt(base64.b64decode(cipher), None)
            print decrypted
            break
        except Exception as ex:
            print ex
            p = gmpy2.next_prime(p**2 + q**2)
            q = gmpy2.next_prime(2*p*q)
            e = gmpy2.next_prime(e**2)
            n = long(p)*long(q)

decrypt_RSA("flag.enc")
