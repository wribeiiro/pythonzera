import sys

args = sys.argv
alphabet = 'abcdefghijklmnopqrstuvwxyz '
salt = 4

def cipher(message, operation):
    alphabet_list = list(alphabet)

    str_ciphered = ''
    for value in message:
        if value in alphabet:
            str_ciphered += alphabet[(alphabet_list.index(value) + (operation * salt)) % len(alphabet_list)]
        else:
            str_ciphered += value

    return str_ciphered

if len(args) <= 2:
    print('you need pass all parameters')
    quit()

if (args[2].lower() == 'encrypt'):
    print(args[1], cipher(args[1], 1))
elif (args[2].lower() == 'decrypt'):
    print(args[1], cipher(args[1], -1))
else:
    print('operation is invalid')
    