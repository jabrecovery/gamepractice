'''Divisible by Ten: loop through numbers and count number of elements divisible by ten.'''

def div_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter
#print(div_by_ten([20, 25, 30, 35, 40]))

'''Greetings: given list of names, attach string to beginning of names.'''

def greetings(names):
    new_list = []
    for name in names:
        new_list.append(f'Hello, {name}')
    return new_list
#print(greetings(['JB', 'KB']))

'''Delete Starting Even Numbers: given list of numbers, return modified list where beginning even numbers are removed.'''

def delete_even_begin(list):
    while len(list) > 0 and list[0] % 2 == 0:
        list = list[1:]
    return list

new = delete_even_begin([4,8,10,11,12,15])
#print(new)


'''Odd Indices: given list, pull out elements at each odd index in list. '''

def odd_index(list):
    new_list = []
    for i in range(1, len(list), 2):
        new_list.append(list[i])
    return new_list
#print(odd_index([4, 3, 7, 10, 11, -2]))

'''Exponents: given list of base, and list of exponents, create a new list of every base take to each exponent'''

def exponent(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base**power)
    return new_list
#print(exponent([2, 3, 4], [1, 2, 3]))

'''Larger Sum: calculate sums of 2 lists, return list with larger sum.'''

def larger_sum(list_1, list_2):
    sum_1 = 0
    sum_2 = 0
    for num in list_1:
        sum_1 += num
    for num in list_2:
        sum_2 += num
    if sum_1 >= sum_2:
        return list_1
    else:
        return list_2
#print(larger_sum([1, 9, 5], [2, 3, 7]))

'''Over 9000: accept list of values, sum values until reaching limit, stop and return value'''

def over_limit(list):
    limit = 0
    for num in list:
        if limit >= 9000:
            return num
        else: 
            limit += num
#print(over_limit([8000, 900, 120, 5000]))

'''Max Num: find max number in given list of numbers.'''

def max_num(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max
#print(max_num([50, -10, 0, 75, 20]))

'''Same Values: accept 2 lists of numbers, create list of indices for matching values in each list.'''

def same_value(list_1, list_2):
    index = []
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            index.append(i)
    return index
#print(same_value([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

'''Reversed List: determine if one list is the same as a second list reversed.'''

def reversed(list_1, list_2):
    if len(list_1) != len(list_2):
        return ('List are different lengths')
    for i in range(len(list_1)):
        if list_1[i] != list_2[len(list_2) - 1 - i]:
            return False
        return True
#print(reversed([1,2,3], [4,2,1,]))
