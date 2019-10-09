#MIXOR


cadena="010100100100010101010100010010010101001001000001010001000100000101000001010000110100111101001110010001100100100101010010010011010100000101010010"
my_hexdata = "06171B19131200040D101A1CO20C1E0C0E01"#Cifra2
#my_hexgata=toHex(cadena)
scale = 16 ## equals to hexadecimal

num_of_bits = 8

a=cadena#bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
b=bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

##resultado=''
##for i in range(len(cripto)):
##    a=cripto[i]
##    b=mes[i]
##    if (bool(a) != bool(b)):
##        resultado+="1"
##    else:
##        resultado+="0"
##
##print(resultado)
