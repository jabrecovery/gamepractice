'''Decipher a coded message given an offset.'''

def decoder(message, key):
    message = message.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''
    for letter in message:
        if letter not in alpha:
            decoded += letter
        else:
            letter = ((alpha.index(letter) + key) % 26)
            new_letter = (alpha[letter])
            decoded += new_letter
    return decoded

key = 10
message = 'Xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
#print(decoder(message, key))

def coder(message, key):
    message = message.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    coded = ''
    for letter in message:
        if letter not in alpha:
            coded += letter
        else:
            letter = ((alpha.index(letter) - key) % 26)
            new_letter = (alpha[letter])
            coded += new_letter
    return coded

key = 10
message = 'Hey there. Thanks for the practice!'
#print(coder(message, key))




message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = 'friends'



def vig_decoder(message, keyword):
    letter_pointer = 0
    key_index = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(message)):
        if message[i] not in alpha:
            key_index += message[i]
        else:
            key_index += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1) % len(keyword)
    translated_message = ''
    for i in range(len(message)):
        if message[i] not in alpha:
            translated_message += message[i]
        else:
            ln = alpha.find(message[i]) - alpha.find(key_index[i])
            translated_message += alpha[ln % 26]
    return translated_message

print(vig_decoder(message, keyword))