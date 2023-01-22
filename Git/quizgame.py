import difflib
print('Welcome to my Quiz Game!')

playing = input('Do you want to play? ')

#use the not equal so the program quits for any response that is not yes, quit functions automatically quits program
if playing.lower() != 'yes':
    quit()
print('Great, let\'s play!')
score = 0

#Question 1 
answer = input('What planet do humans live on? ')
if answer.lower() == 'earth':
    print('Correct')
    score += 1
else: 
    print('Incorrect')

#Question 2 
answer = input('What is the name of my dog? ')
if answer.lower() == 'mattis':
    print('Correct')
    score += 1
else: 
    print('Incorrect')

print('Your score is ' + str(score) + ' points.')
print('Your score is ' + str((score / 2)* 100) + ' %.')