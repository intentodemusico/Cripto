# ---------------------------- Playfair Cypher ---------------------------- #
# This Python code is for encrypting purposes. The algorithm executes a     #
# Playfair cypher                                                           #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
from collections import OrderedDict

def normalize_text(plain_text):
    plain_text = plain_text.upper()
    plain_text = plain_text.replace('Á', 'A')
    plain_text = plain_text.replace('É', 'E')
    plain_text = plain_text.replace('Í', 'I')
    plain_text = plain_text.replace('Ó', 'O')
    plain_text = plain_text.replace('Ú', 'U')
    plain_text = re.sub('(?![A-Z]).', '', plain_text)
    plain_text = re.sub(' +', '', plain_text)
    return plain_text

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

plain_text = input('Enter the text to be encrypted: ')

plain_text = normalize_text(plain_text)
len_text = len(plain_text)
replaced_text = plain_text

index = 0
caracter = ''
for i in range(0,len(plain_text)-1):
    if plain_text[i] == plain_text[i+1]:
        if plain_text[i+1] != 'X':
            caracter = 'X'
        else:
            caracter = 'Z'
        replaced_text = replaced_text[:index+1] + caracter + replaced_text[index+1:]
        index += 1
    index += 1

len_text = len(replaced_text)
if len_text%2 == 1:
    if replaced_text[len(replaced_text)-1] == 'X':
        replaced_text += 'Z'
    else:
        replaced_text += 'X'
        
encrypted_text = ''

for i in range(0,len_text,2):
    tuple_i1 = (dictionary[replaced_text[i]]//5, dictionary[replaced_text[i]]%5)
    tuple_i2 = (dictionary[replaced_text[i+1]]//5, dictionary[replaced_text[i+1]]%5)
    if tuple_i1[0] == tuple_i2[0]:
        encrypted_text += dictionary_lst[tuple_i1[0]*5+(tuple_i1[1]+1)%5]
        encrypted_text += dictionary_lst[tuple_i2[0]*5+(tuple_i2[1]+1)%5]
    elif tuple_i1[1] == tuple_i2[1]:
        encrypted_text += dictionary_lst[(((tuple_i1[0]+1)*5)%25)+(tuple_i1[1]%5)]
        encrypted_text += dictionary_lst[(((tuple_i2[0]+1)*5)%25)+(tuple_i2[1]%5)]
    else:
        encrypted_text += dictionary_lst[(tuple_i1[0]*5)+(tuple_i2[1]%5)]
        encrypted_text += dictionary_lst[(tuple_i2[0]*5)+(tuple_i1[1]%5)]
    if (i+2)%8==0 and i+2>0: encrypted_text += ' '
    #print(replaced_text[i] + '' + replaced_text[i+1],end = ' ')

print('Playfair encryption result: ' + encrypted_text)
