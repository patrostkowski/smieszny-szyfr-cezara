#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random, sys

alfabet = '3aKbcL4dMefN5OghPiR6SjTkUlV7mWAnXoB8YpCq9ZDrsE0tFu1vGwHx2IyzJ'
alen = len(alfabet)
tekst_we1 = "hej"
tekst_we2 = "xu3Nq9"
znak     = ""
przes = 40
indx     = 0
code=True
rand_num = random.randint(10,50)

#with open('encrypted','r') as f:
#    enc_tekst = f.read().splitlines()

#with open('decrypted','r') as f:
#    dec_tekst = f.read().splitlines()


def encrypt(tekst_we):
    tekst_wy = ""
    przes = rand_num
    for znak in tekst_we:
        indx = alfabet.find(znak)
        if indx != -1 :
            tekst_wy += alfabet[ (indx + przes) % len(alfabet) ]
        else:
            tekst_wy += znak
    for x in range (len(tekst_we)-1):
        tekst_wy += alfabet[random.randint(0,len(alfabet)-1)]
    tekst_wy += alfabet[przes]
    print("Tekst wyjściowy to: " + tekst_wy)
    return tekst_wy

def decrypt(tekst_we):
    custom_len = len(tekst_we)/2
    tekst_wy = ""
    temp = tekst_we[-1]
    przes = alfabet.find(temp)
    for znak in tekst_we:
        indx = alfabet.find(znak)
        if indx != -1 :
            tekst_wy += alfabet[ (indx - przes) % len(alfabet) ]
        else:
            tekst_wy += znak
    tekst_wy = tekst_wy[:-int(custom_len)] 
    print("Tekst wyjściowy to: " + tekst_wy)
    return tekst_wy

def full_encryption(zdanie):
    enc_sentence = ''
    temp = zdanie.split()
    print(temp)
    for x in temp:
        enc_sentence += encrypt(x) + ' '
    return enc_sentence[:-1]

def full_decryption(zdanie):
    enc_sentence = ''
    temp = zdanie.split()
    print(temp)
    for x in temp:
        enc_sentence += decrypt(x) + ' '
    return enc_sentence[:-1]

#print(full_decryption(full_encryption('ladna pogoda dzisiaj')))



