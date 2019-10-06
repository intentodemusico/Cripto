#Script supremo para hallar IC e IF

# Tomado de "03-Kasiski_Method.py" como material de clase
from operator import itemgetter
import re
import itertools
########################

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

def letters_count(cryptogram):
    word_dict = {}
    for char in cryptogram:
        if char in word_dict:
            word_dict[char] = word_dict[char] + 1;
        else:
            word_dict[char] = 1;

    word_dict.pop(' ', None)
    word_dict.pop('\n', None)

    return sorted(word_dict.items(), key=itemgetter(1), reverse=True)

def dictionary_toString(dictionary_diff, MAXLEN):
    print('n-gram' + ' '*(MAXLEN-len('n-gram')+1)+'\t' + 'Distance')
    for key in dictionary_diff:
        print(key, end=' '*(MAXLEN-len(key)+1)+'\t')
        print(dictionary_diff[key])

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

# ---------------------------------- Program ------------------------------ #

# Cryptogram input
cryptogram = normalize_text(input('Enter the text: '))

# Letters count
word_lst = letters_count(cryptogram)
word_dict = dict(word_lst)


# IC calculation
N = sum(word_dict.values())
IC = 0

for character in word_dict:
    IC += word_dict[character]*(word_dict[character]-1)
IC /= (N*(N-1))
IC -= 0.0032

print('\n-------------------- IC value --------------------')
print('IC value: ' + str(IC))

print('\n-------------------- IF value --------------------')
print('IF value: ' + str(get_IF(letters_count(word_dict))))
