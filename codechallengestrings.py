'''Count Letters: count the number of unique letters in string.'''

def letter_counter(word):
    letter_couter = 0
    alpha_tracker = []
    for letter in word:
        if letter not in alpha_tracker:
            alpha_tracker.append(letter)
            letter_couter += 1
    return letter_couter, alpha_tracker

word_check = letter_counter('mississippi')
#print(word_check)

'''Count X: count number of occurances of provided value in given string'''

def value_counter(word, x):
    word = word.lower()
    x_counter = 0
    for letter in word:
        if letter == x:
            x_counter += 1
    return x_counter
x_check = value_counter('MISSISSIPPI', 'i')
#print(x_check)

'''Count Multi-X: compare the number of occurances of one string within a different string'''
def string_counter(word, sub):
    sub_counter = 0
    word_split = []
    word_split.append(word.split(sub))
    return len(word_split)
check = string_counter('subsub', 'sub')
#print(check)

'''Substring Between: extract a portion of a string between 2 given characters.'''

def string_between(string, x, y):
    start = string.find(x)
    end = string.find(y)
    if start != -1 or end != -1:
        return string[start+1:end]
    
#print(string_between("apple", "p", "e"))

'''X Length: Accept string and number, compare length of each word to the given number. Can change the comparison to number to compare smaller or larger lengths too.'''

def x_length(word, x):
    word = word.split(' ')
    for i in range(len(word)):
        if len(word[i]) != x:
            return False
        else:
            return True
#print(x_length("i like apples", 2))

'''Check Name: Accept string and name, check if name is within string.'''
def check_name(string, name):
    return name.lower() in string.lower()

#print(check_name('My name is JB', 'jb'))

'''Every Other Letter: extract and return every other letter from given string'''
def every_other(string):
    new_string = ''
    for i in range(0, len(string), 2):
        new_string += string[i]
    return new_string
#print(every_other('Codecademy'))

'''Reverse: reverse the given string'''
def reverse(string):
    new_string = ''
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string
#print(reverse('jab'))

'''Make Spoonerism: switch the first 2 letters of given string'''
def spoonerism(word_1, word_2):
    word_1_first = word_2[0] + word_1[1:]
    word_2_first = word_1[0] + word_2[1:]
    return word_1_first + ' ' + word_2_first
#print(spoonerism('Hello', 'World'))

'''Add Exclamation: Add exclamation points up to 20 characters, or if string is 20 characters return the string'''
def add_exclamation(string):
    while len(string) < 20:
        string += '!'
    return string
print(add_exclamation('hello'))


     