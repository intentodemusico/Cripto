# -------------------------- Scytale Decryption --------------------------- #
# This Python code is for decryption purposes. Scytale Decryption method    #
# is applied to a simple text.                                              #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
import pickle

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

def padding_number(cryptogram, columns):
    return ((-len(cryptogram))%columns)

def Scytale_decrypt(cryptogram, columns):
    out = ''
    pad = padding_number(cryptogram, columns)
    rows = len(cryptogram+' '*((-len(cryptogram))%columns))//columns
    flag = True
    for i in range(0, rows):
        out += cryptogram[i:((columns+1-pad)*rows)+i:rows]
        out += cryptogram[((columns+1-pad)*rows)+i-1::rows-1]
    out = re.sub(' ', '', out)
    return out[:len(cryptogram)]

##columns = int(input('Enter the number of columns for encryption: '))
##while(columns < 2):
##    columns = int(input('Enter the number of columns for encryption: '))
cryptogram = "CEAILLFAAREASDCOIDT"#input('Enter the text to be encrypted: ')
for i in range(2,len(cryptogram)):
    columns=i
    cryptogram = normalize_text(cryptogram)
    print("Columns:",columns)
    print('Scytale decryption result: ' + Scytale_decrypt(cryptogram, columns))
