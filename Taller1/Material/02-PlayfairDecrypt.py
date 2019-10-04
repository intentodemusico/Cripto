# --------------------------- Playfair Decrypt ---------------------------- #
# This Python code is for Decryption purposes. The algorithm executes a     #
# Playfair decryption                                                       #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
from collections import OrderedDict

def normalize_text(cryptogram):
    cryptogram = cryptogram.upper()
    cryptogram = cryptogram.replace('Á', 'A')
    cryptogram = cryptogram.replace('É', 'E')
    cryptogram = cryptogram.replace('Í', 'I')
    cryptogram = cryptogram.replace('Ó', 'O')
    cryptogram = cryptogram.replace('Ú', 'U')
    cryptogram = re.sub('(?![A-Z]).', '', cryptogram)
    cryptogram = re.sub(' +', '', cryptogram)
    return cryptogram

dictionary = {}
lst = []
for i in range(0,26):
    if chr(i+65) is not 'J':
        lst.append(chr(i+65))

key = input("Enter the key: ")
key = normalize_text(key)
key = "".join(OrderedDict.fromkeys(key[0:25]))
key = key.upper()
key = key.replace('J', 'I')

cont = 0
for i in range(0,len(key)):
    dictionary[key[i]] = cont
    lst.remove(key[i])
    cont += 1

for i in range(0,len(lst)):
    dictionary[lst[i]] = cont
    cont += 1

dictionary['J'] = dictionary['I']
dictionary_lst = list(dictionary)

cryptogram = input('Enter the cryptogram to be decrypted: ')

cryptogram = normalize_text(cryptogram)
len_text = len(cryptogram)
       
decrypted_text = ''

for i in range(0,len_text-1,2):
    tuple_i1 = (dictionary[cryptogram[i]]//5, dictionary[cryptogram[i]]%5)
    tuple_i2 = (dictionary[cryptogram[i+1]]//5, dictionary[cryptogram[i+1]]%5)
    if tuple_i1[0] == tuple_i2[0]:
        decrypted_text += dictionary_lst[tuple_i1[0]*5+(tuple_i1[1]-1)%5]
        decrypted_text += dictionary_lst[tuple_i2[0]*5+(tuple_i2[1]-1)%5]
    elif tuple_i1[1] == tuple_i2[1]:
        decrypted_text += dictionary_lst[(((tuple_i1[0]-1)*5)%25)+(tuple_i1[1]%5)]
        decrypted_text += dictionary_lst[(((tuple_i2[0]-1)*5)%25)+(tuple_i2[1]%5)]
    else:
        decrypted_text += dictionary_lst[(tuple_i1[0]*5)+(tuple_i2[1]%5)]
        decrypted_text += dictionary_lst[(tuple_i2[0]*5)+(tuple_i1[1]%5)]

print('Playfair decryption result: ' + decrypted_text)
