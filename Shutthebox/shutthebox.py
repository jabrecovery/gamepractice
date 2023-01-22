import random

print("Welcome to Shut the Box!")

start_num = [1, 2, 3, 4, 5, 6]

while len(start_num) > 0:
    num = random.randint(1,6)
    print(num)
    print('Choose a number to remove.')
    user_num = input()
    start_num.remove(int(user_num))
    if num not in start_num:
        print('The game is over!')
        print(sum(start_num))
    print(start_num)



#class Game:
   # num_1 = random.randint(1,6)
   # num_2 = random.randint(1,6)
    #print(num_1, num_2)
    #begin_num = [1,2,3,4,5,6,7,8,9]

#while begin_num
#begin_num = [1,2,3,4,5,6,7,8,9]
#print("Choose a number to remove.")
#user_selection = input()
#game_num = begin_num.remove(int(user_selection))
#print(begin_num)

















