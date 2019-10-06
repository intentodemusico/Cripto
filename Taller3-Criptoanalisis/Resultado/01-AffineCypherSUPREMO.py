# ----------------------------- Affine Cypher ----------------------------- #
# This Python code is for encrypting purposes. The algorithm executes a     #
# substitution cypher according to the equation: C = (a*M + b) mod (n).     #
# Author: Julián Darío Miranda                                              #
# Institution: Pontifical Bolivarian University, Bucaramanga, Colombia      #
# Subject: Information Security Specialization                              #
# ------------------------------------------------------------------------- #

import re, os
import numpy as np
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

##x=normalize_text("Ay perrito pénsjajs")
##
##for elemento in x:
##    print(elemento)
##
##
##a = input("Enter the 'a' value: ")
##while not a.isdigit(): a = input("Enter a correct 'a' value: ")
##a = int(a)
##    
##b = input("Enter the 'b' value: ")
##while not b.isdigit(): b = input("Enter a correct 'b' value: ")
##b = int(b)
##
##plain_text = input('Enter the text to be encrypted: ')
##
##replaced_text = normalize_text(plain_text)
##len_text = len(replaced_text)

letras = ['A','B','C','D','E','F','G','H','I','J','K','U','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
maFrecuencia=["E","A","O","S","N","R"]
meFrecuencia=["F","J","Z","X","K","W"]
##def devolverIf(cadena,lista):
    
def j(text):
    a=1
    for b in range(26):
        textCr=normalize_text(text)
        conteo=np.zeros(26)
        for i in range(0,len(textCr)):
            if textCr[i] is not " ":
                textCr = textCr[:i] + chr((a*(ord(textCr[i])-65) + b)%26 + 65) + textCr[i+1:]
        
##        for letraI in range(26):
##            c = textCr.count(letras[letraI])
##            conteo[letraI]=c
##            
##            print("Conteo:",conteo)
##
##
##            ##
##            sorted(dic.items(), key=lambda dic: dic[1])

        ##print("Letra:",letra, "= ",c)
        print("Affine encryption result: " + textCr)

j("OBOTXELNEMTGWXFTKKNXVHLXEFTKKHJNBTETUTKTLNGHFUKXIHKJNXXELNEMTGTWHLXKTLNIKHIBXMTKBHIHKLBXFIKX")
