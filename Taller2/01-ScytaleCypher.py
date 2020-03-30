# ---------------------------- Scytale Cypher ----------------------------- #
# This Python code is for cryptography purposes. Scytale Encrypting         #
# method is  applied to a simple text.                                      #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
import pickle

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

def padding_set(plain_text, columns):
    plain_text += ' '*((-len(plain_text))%columns)
    return plain_text

def Scytale_encrypt(plain_text, columns):
    out = ''
    for i in range(0, columns):
        out += plain_text[i::columns]
    out = re.sub(' ', '', out)
    return out
plain_text = "ESTAMOS LISTOS PARA EL COMBATE"#input('Enter the text to be encrypted: ')
#for i in range(1,27):
    #print("I:",i)
columns = 21#i #int(input('Enter the number of columns for encryption: '))
##while(columns < 2):
##    columns = int(input('Enter the number of columns for encryption: '))
plain_text = normalize_text(plain_text)
len_text = len(plain_text)
plain_text = padding_set(plain_text, columns)

print('Scytale encryption result: ' + Scytale_encrypt(plain_text, columns))
