import random

top_of_range = input('Type a number: ')

"""user input will be a string, need to convert to integer, need to check if input is a digit and larger than 0"""

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type number larger than 0')
        quit()
else:
    print('Please type a number next time.')
    quit()


r = random.randint(0, top_of_range)
guesses = 0
#print(r)

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        #continue takes loop back to beginning
        continue

    if user_guess == r:
        print('You got it!')
        #breaks loop for correct answer
        break
    elif user_guess > r:
        print('Your guess is above the number!')
    else:
        print('Your guess is below the number!')

#commas remove the need for the + signs and string
print('You got it in', guesses, 'guesses.')