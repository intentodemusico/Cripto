# ------------------- Breaking Substitution Encryption -------------------- #
# This Python code is for decrypting an encrypted text, using frequency     #
# analysis. The text was initially encrypted with sustitution algorithms    #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
from operator import itemgetter
import pickle

# ---------------------------------- Methods ------------------------------ #
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

def get_dict_freq_as_list(encrypt_text):
    encrypt_freq_dict = {}
    for char in encrypt_text:
        if char in encrypt_freq_dict:
            encrypt_freq_dict[char] = encrypt_freq_dict[char] + 1;
        else:
            encrypt_freq_dict[char] = 1;
    return sorted(encrypt_freq_dict.items(), key=itemgetter(1), reverse=True)

def get_IF(freq_dict):      
    first_five_letters = ['E', 'A', 'O' , 'S' , 'N' , 'R']
    last_five_letters = ['F', 'J', 'Z' , 'X' , 'K' , 'W']
    IF = 0
    for i in range(0, 5):
        if freq_dict[i][0] in first_five_letters:
            IF += 1
    for i in range(-1, -6):
        if freq_dict[i][0] in last_five_letters:
            IF += 1
    return IF

def decrypt(cryptogram, a, b):
    text = cryptogram
    len_cryptogram = len(text)
    for i in range(0,len_cryptogram):
        if text[i] is not " ":
            text = text[:i] + chr((a*(ord(text[i])-65) - b)%26 + 65) + text[i+1:]
    return text
# --------------------------------- Variables ----------------------------- #
cont = 5
path = 'Files/'
file = path + 'Text' + str(cont) + '_SubsMono_Encrypt.txt'
mayor = -1
# ---------------------------------- Program ------------------------------ #
encrypt_text = normalize_text(input('Enter the cryptogram: '))

possible_messages = {}

print('\n----- IF values while the b-key is changed for decryption ------')
print('Key\tDecryption Result\tIF')
for b in range(0,27):
    decrypted_text = decrypt(encrypt_text, 1, b)
    IF = get_IF(get_dict_freq_as_list(decrypted_text))
    if IF > mayor:
        possible_messages = {}
        mayor = IF
        possible_messages[b] = decrypted_text
    elif IF == mayor:
        possible_messages[b] = decrypted_text
    print(' ' + str(b) + '\t' + decrypted_text[0:20] + '\t' + str(IF))

print('\n----------------- Most Probable key values -----------------------')
for message in possible_messages:
    print('- ' + str(message) + ': ' + possible_messages[message][0:75])
    
    
