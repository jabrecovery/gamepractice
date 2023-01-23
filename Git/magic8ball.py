import random

#Creat a magic 8 ball game. User inputs name and question and gets one of the following responses. Then allows person to exit or ask another question.


responses = {
    1: 'Yes - definitely.',
    2: 'It is decidedly so.',
    3: 'Without a doubt.',
    4: 'Reply hazy, try again.',
    5: 'Ask again later.',
    6: 'Better not tell you now.',
    7: 'My sources say no.',
    8: 'Outlook not so good.',
    9: 'Very doubtful.'
}

def the_game():
    user_name = input('What is your name? ')
    print(f'Welcome to the Magic 8 Ball, {user_name}')

    while True:
        user_question = input('Ask me your question.....')
        
        random_choice = random.randint(1,9)

        response_to_question = responses[random_choice]

        print(f'The Magic 8 Ball thinks.....{response_to_question}')

        another_question = input('Do you have another question? Type y or n.').lower()

        if another_question == 'y':
            continue
        
        elif another_question == 'n':
            break
    
    print('Goodbye and good fortune!')

the_game()



