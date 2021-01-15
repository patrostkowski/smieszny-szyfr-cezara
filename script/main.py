#!/usr/bin/env python3

import random, sys

alpha = '3aKbcL4dMefN5OghPiR6SjTkUlV7mWAnXoB8YpCq9ZDrsE0tFu1vGwHx2IyzJ'
alen = len(alpha)
tekst_we1 = "hej"
tekst_we2 = "xu3Nq9"
indx     = 0

def encrypt(tekst_we):
    rand_num = random.randint(10,50)
    tekst_wy = ""
    przes = rand_num
    for znak in tekst_we:
        indx = alpha.find(znak)
        if indx != -1 :
            tekst_wy += alpha[ (indx + przes) % len(alpha) ]
        else:
            tekst_wy += znak
    for _ in range (len(tekst_we)-1):
        tekst_wy += alpha[random.randint(0,len(alpha)-1)]
    tekst_wy += alpha[przes]
    return tekst_wy

def decrypt(tekst_we):
    custom_len = len(tekst_we)/2
    tekst_wy = ""
    temp = tekst_we[-1]
    przes = alpha.find(temp)
    for znak in tekst_we:
        indx = alpha.find(znak)
        if indx != -1 :
            tekst_wy += alpha[ (indx - przes) % len(alpha) ]
        else:
            tekst_wy += znak
    tekst_wy = tekst_wy[:-int(custom_len)] 
    return tekst_wy

def full_encryption(zdanie):
    enc_sentence = ''
    temp = zdanie.split()
    for x in temp:
        enc_sentence += encrypt(x) + ' '
    return enc_sentence[:-1]

def full_decryption(zdanie):
    enc_sentence = ''
    temp = zdanie.split()
    for x in temp:
        enc_sentence += decrypt(x) + ' '
    return enc_sentence[:-1]

ans=True
while ans:
    print ("""
    1.Zakoduj wiadmosc.
    2.Odkoduj wiadmosc.
    3.Exit.\n
    """)
    ans=input("Co chcialbys zrobic?:") 
    if ans=="1": 
        value = input('Wpisz wiadmosc do zakodowania: ')
        print(f'Zakodowana wiadomosc to: {full_encryption(value)}')
        print('\n')
    elif ans=="2":
        value = input('Wpisz wiadomosc do odkodowania: ')
        print(f'Zakodowana wiadomosc to: {full_decryption(value)}')
        print('\n')
    elif ans=="3":
        print("\n Do nastepnego!")
        ans = None
        sys.exit()
    elif ans !="":
        print("\n Blad!") 

