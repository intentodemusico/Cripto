# ---------------------------- ADFGVX Cypher ------------------------------ #
# This Python code is for cryptography purposes. ADFGVX Encrypting          #
# method is  applied to a simple text.                                      #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
import pickle
import numpy as np

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

def matrix_generation():
    dictionary = {}
    lst = []
    init_val= 65
    end_val = init_val + 26

    for a in range(init_val, end_val):
        lst.append(chr(a))

    for a in range(0, 10):
        lst.append(str(a))

    total = len(lst)

    for i in range(0, total):
        number = np.random.randint(0, len(lst))
        element = lst.pop(number)
        dictionary[element] = (i//6,i%6)
    return dictionary

def matrix_read(file, separator):
    dictionary = {}
    cont = 0
    if(os.path.isfile(file)):
        with open(file, 'r') as content_file:
            for line in content_file:
                column = line.split(separator)
                for col in column:
                    dictionary[col.replace('\n','')] = (cont//6,cont%6)
                    cont += 1
    return dictionary

def matrix_toString(dictionary):
    lst = list(dictionary)
    for i in range(0, 36):
        if i%6 == 0: print()
        element = lst[i]
        #print(element,end='\t')

def padding_set(plain_text, columns):
    plain_text += ' '*((-len(plain_text))%columns)
    return plain_text

def key_sort(key):
    key_bis = []
    key = list(key)
    len_key = len(key)
    for i in range(0,len_key): key_bis.append((key[i],0))
    flag = False
    lst = []
    for i in range(0,len_key):
        menor = i
        for ii in range(i+1,len_key):
            if ord(key[ii])<ord(key[menor]):
                menor = ii
                flag = True
        if flag:
            tmp = key[i]
            key[i] = key[menor]
            key[menor] = tmp
        index = key_bis.index((key[i],0))
        lst.append(key_bis.index((key[i],0)))
        key_bis[index] = (key_bis[index][0],1)
        flag = False
    return lst

path = ''
name = 'Random_Matrix_1.txt'
file = path+name
separator = ';'
lst = ['A','D','F','G','V','X']
matrix_cols = []

plain_text = input('Enter the text to be encrypted: ')
for i in range(3):
    plain_text = normalize_text(plain_text)
    len_text = len(plain_text)

    key = input('Enter the key: ')
    key = normalize_text(key)
    len_key = len(key)

    matrix = matrix_read(file, separator)
    #matrix = matrix_generation()
    #matrix_toString(matrix)
    print(" ")
    string = ''
    for i in range(0, len_text):
        value = matrix[plain_text[i]]
        string += lst[value[0]] + lst[value[1]]

    string = padding_set(string, len_key)

    order = key_sort(key)
    for i in range(0,len_key):
        matrix_cols.append(string[order[i]::len_key])

    result = ''
    for column in range(0,len(matrix_cols)):
        result += ''.join(matrix_cols[column])
    result = result.replace(' ','')
    print('ADFGVX encryption result: ' + result)
        


