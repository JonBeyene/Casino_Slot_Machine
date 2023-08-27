import random

# slot machine will have 4 lines always
NUM_LINES = 4
# minimum bet value
MIN_BET = 1
# maximum bet value
MAX_BET = 100
# number of rows in slot machine
ROW = 4
# number of columns in slot machine
COLS = 3

symbol_count = {
    '*': 2,
    '#': 3,
    '&': 4,
    '@': 5
}

multiplier_value = {
    '*': 10,
    '#': 6,
    '&': 4,
    '@': 2
}


def slot_machine_spin(rows, cols, symbols):
    # creates a list with the symbols and the correct amount
    # ie. [*, #, #, #, &, &, &, &, @, @, @, @, @, @]
    possible_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            possible_symbols.append(symbol)

    # represents the columns of a slot machine
    column_ticker = []
    for _ in range(cols):
        column = []
        amendable_symbols = possible_symbols[:]
        for _ in range(rows):
            item = random.choice(amendable_symbols)
            amendable_symbols.remove(item)
            column.append(item)

        column_ticker.append(column)

    return column_ticker


def visual_slot_machine(columns):
    # transposes initial matrix holding symbol values
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_win(columns, num_lines, bet_val, values):
    money = 0
    winning_lines = []
    for line in range(num_lines):
        symbol = columns[0][line]
        for column in columns:
            check = column[line]
            if symbol != check:
                break
        else:
            money += values[symbol] * bet_val
            winning_lines.append(line + 1)

    return money, winning_lines




def deposit_balance():
    # keeps looping until user provides valid input
    while True:
        input_amount = input('How much are you depositing? $')
        # determines if valid input is number
        if input_amount.isdigit():
            input_amount = int(input_amount)
            if input_amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number value')
    return input_amount


def lines():
    while True:
        amount_lines = input(f'Enter the number of lines you would like to bet on (1 - {NUM_LINES})? ')
        if amount_lines.isdigit():
            amount_lines = int(amount_lines)
            if 1 <= amount_lines <= NUM_LINES:
                break
            else:
                print('Input a valid number of lines')
        else:
            print('Please enter a number value')
    return amount_lines


def bet():
    while True:
        bet_amount = input('What amount would you like to bet per line? $')
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f'Bet amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a number value')
    return bet_amount


def game(balance):
    line = lines()
    while True:
        bets = bet()
        total_bet = line * bets
        if total_bet > balance:
            print(f'You do not have sufficient funds. Your current balance is: ${balance}')
        else:
            break
    print(f'You are betting ${bets} each on {line} lines with a total bet equal to ${total_bet}')

    spin = slot_machine_spin(ROW, COLS, symbol_count)
    visual_slot_machine(spin)
    winnings, winning_lines = check_win(spin, line, bets, multiplier_value)
    print(f'You won ${winnings}')
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet

def main():
    account_balance = deposit_balance()
    while True:
        print(f'Current balance is: ${account_balance}')
        spin = input('Press enter to play or q to quit')
        if spin == 'q':
            break
        account_balance += game(account_balance)

    print(f'You left with ${account_balance}')


main()
