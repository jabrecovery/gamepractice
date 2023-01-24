'''Every Three Numbers: create list of numbers, up to 100, every 3 numbers.'''

def every_three(start, end, jump):
    new_list = list(range(start, end, jump))
    return new_list
new_list = every_three(0, 101, 3)
#print(new_list)

'''Remove middle: remove elements from list given starting and ending index'''

def remove_middle(list, start, end):
    return list[:start] + list[end+1:]
new_list = remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
#print(new_list)

'''More Frequent Item: accept list, count x and y occurances in list, return greater.'''

def more_freq(list, x, y):
    if list.count(x) >= list.count(y):
        return x
    else:
        return y
answer = more_freq([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3)
#print(answer)

'''Double Index: double value at given position. Given list and index.'''
def double_index(list, x):
    if x >= len(list):
        return list
    else:
        new = list[:x]
        new.append(list[x]*2)
        new = new + list[x+1:]
        return new
answer = double_index([1,2,3,4], 2)
#print(answer)

'''Middle Item: find middle item from list. Given a list, detemine even or odd length, even return average of middle 2, odd return middle'''

def middle_item(list):
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)-1] + list[int(len(list)/2)]) /2
    else: 
        num = int((len(list) / 2) - 0.5)
        return list[num]

print(middle_item([1,2,3,4,5]))

        