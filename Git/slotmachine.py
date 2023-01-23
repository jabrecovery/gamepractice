import random

#provides constant for the betting lines, use variable in the code below, can update this constant at any point 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#set up the rows and columns for slot machine
ROWS = 3
COLS = 3

#dictionary for the number of possibilites for each row/symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
#the amount for each symbol, can update
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#find the first symbol in each row and compare to the other symbols, looks at the first symbol for the line being looked at
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

#create a function that randomly selects the symbols for each row, then removes that symbol from the possibilites for the next row, repeat this for each column
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    #loops through the above dictionary and adds that symbol to list for the slot spin
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #the colon is a splice operator so that it removes any choice so you only have the allowed amount from the above dictionary. 
    #define the column list, for loop will repeat for the number of columns in the above range of the slot machine, current symbols is equal to the values thta remain after each loop, which removes the symbol if chosen in the any of the loops
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


#this is a matrix and we need to transpose the matrix. check for i in the range so that only 2 pipes are printed to look like slot machine, end tells print statement 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=' | ')
            else:
                print(column[row], end="")
        #adds a row in between each row on the slot machine
        print()


#create a while loop to get the correct input, check for valid input and then convert from string to integer, then return the amount
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINES:
                break
            else:
                print('Enter correct number of lines.')
        else:
            print("Please enter a number.")

    return lines

def get_bet_amount():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print('Please enter a number.')
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough funds to make that bet. Your current balance is: ${balance}')
        else: 
            break
   
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won {winnings}.')
    #the * is splat function 
    print(f"You won on", *winning_lines)
    return winnings - total_bet

#balance begins everything for the gamble game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input('Press enter to play or q to quit.').lower()
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f'You left with ${balance}.')


main()


