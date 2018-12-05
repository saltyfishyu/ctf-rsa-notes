# 0ctf - RSA

	>Tip: openssl rsautl -encrypt -in FLAG -inkey public.pem -pubin -out flag.enc

#openssl rsa -in public.pem -pubin -text -modulus
```
Public-Key: (314 bit)
Modulus:
    02:ca:a9:c0:9d:c1:06:1e:50:7e:5b:7f:39:dd:e3:
    45:5f:cf:e1:27:a2:c6:9b:62:1c:83:fd:9d:3d:3e:
    aa:3a:ac:42:14:7c:d7:18:8c:53
Exponent: 3 (0x3)
Modulus=2CAA9C09DC1061E507E5B7F39DDE3455FCFE127A2C69B621C83FD9D3D3EAA3AAC42147CD7188C53
writing RSA key
-----BEGIN PUBLIC KEY-----
MEEwDQYJKoZIhvcNAQEBBQADMAAwLQIoAsqpwJ3BBh5Qflt/Od3jRV/P4Seixpti
HIP9nT0+qjqsQhR81xiMUwIBAw==
-----END PUBLIC KEY-----
```
#n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067

#e = 3

#factor n

#p = 26440615366395242196516853423447

#q = 27038194053540661979045656526063

#r = 32581479300404876772405716877547

We get 3 prime numbers. This is still fine, this could simply be multiprime RSA
```
ciphertext = plaintext^e mod n = (plaintext^e')^3 mod n
```
```
ciphertext = plaintext^3 mod n
```
then we do these things.

#python pt.py

we get these things(Chinese Reminder Theorem)
```
pt^3 mod p = ciperhtext mod p = 20827907988103030784078915883129
```
```
pt^3 mod q = ciperhtext mod q = 19342563376936634263836075415482
```
```
pt^3 mod r = ciperhtext mod r = 10525283947807760227880406671000
```
we figured that wolframalpha had this implemented

https://www.wolframalpha.com/input/?i=x%5E3+%3D+20827907988103030784078915883129+(mod+26440615366395242196516853423447)

https://www.wolframalpha.com/input/?i=x%5E3+%3D+19342563376936634263836075415482+(mod+27038194053540661979045656526063)

https://www.wolframalpha.com/input/?i=x%5E3+%3D+10525283947807760227880406671000+(mod+32581479300404876772405716877547)

This gives us a set of possible solutions:
```
root0 = [5686385026105901867473638678946, 7379361747422713811654086477766, 13374868592866626517389128266735]
root1 = [19616973567618515464515107624812]
root2 = [6149264605288583791069539134541, 13028011585706956936052628027629, 13404203109409336045283549715377]
```

#python exp.py
```
��ڳ�g�%�	F���������F�7���j
                                  s����i
�^˄�RC�J0ctf{HahA!Thi5_1s_n0T_rSa~}

.�Y~U���#{��ʨ�[��E����n����T�_�s
-���ϵ����
         =/gN49�UM�
BRD:�03�����ǈnf��'f������ f�y�
nd���Z��x��ݵ�G���
oC�^�����1��e
c�;
�/X����o[���o9���~`i~��PtP920H
����/�r{B�v�"$?S%���}?>0^�+~	k\�R<
�4�O�Z���	�����2��"���+���l��e�
```