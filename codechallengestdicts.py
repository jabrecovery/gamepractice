'''Sum Values: sum each value from given dictionary'''
def sum_values(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum
print(sum_values({"milk":5, "eggs":2, "flour": 3}))

'''Even Keys: accept dictionary, sum values from only even keys'''
def even_keys(dict):
    sum = 0
    for key, value in dict.items():
        if key % 2 == 0:
            sum += value
    return sum
#print(even_keys({1:5, 2:2, 3:3}))

'''Add Ten: Given dictionary, add 10 to each value and return dictionary'''
def add_ten(dict):
    for key, value in dict.items():
        dict[key] = value + 10
    return dict
#print(add_ten({1:5, 2:2, 3:3}))

'''Values that are keys: Given dictionary, look for values that are also keys, and store those values in separate list.'''
def key_value_pairs(dict):
    pairs = []
    for value in dict.values():
        if value in dict.keys():
            pairs.append(value)
    return pairs
#print(key_value_pairs({1:100, 2:1, 3:4, 4:10}))

'''Largest Value: look for largest value in dictionary and return the key'''
def largest_value(dict):
    begin_key = -1
    begin_value = -1
    for key, value in dict.items():
        if value > begin_value:
            begin_value = value
            begin_key = key
    return begin_key
#print(largest_value({1:100, 2:1, 3:4, 4:10}))

'''Word Length Dict: create dictionary given string, keys are words in string and values are length of word'''
def word_length(*strings):
    dict = {}
    for word in strings:
        dict[word] = len(word)
    return dict
#print(word_length('apple', 'dog', 'world'))

'''Frequency Count: given list of strings, create dictionary that counts the frequency of each string'''
def freq_count(strings):
    dict = {}
    for word in strings:
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    return dict
#print(freq_count(["apple", "apple", "cat", 1]))

'''Unique Values: count unique freqs of values in given dictionary'''
def unique_value(dictionary):
    list = []
    for value in dictionary.values():
        if value not in list:
            list.append(value)
    return len(list)
#print(unique_value({0:3, 1:1, 4:1, 5:3}))

'''Count First Letter: Given dictionary, count individuals with same first letter of values for each key'''
def count_first(dictionary):
    dict = {}
    for key, value in dictionary.items():
        ln = value[0]
        if ln not in dict.keys():
            dict[ln] = 1
        else:
            dict[ln] += 1
print(count_first({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))