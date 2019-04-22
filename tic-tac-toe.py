def play():
    while True:
        table_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print('Welcome to Tic Tac Toe game!')
        players = x_or_o()
        player1 = players[0]
        player2 = players[1]
        if not yes_or_no():
            break
        game(table_list, player1, player2)
        if not replay():
            break


def game(list, a, b):
    while True:
        print('\n' * 100)
        print_table(list)
        player1_input(list, a)
        if (list[0] == a and list[1] == a and list[2] == a) or (list[0] == a and list[3] == a and list[6] == a) or (
                list[0] == a and list[4] == a and list[8] == a) or (list[1] == a and list[4] == a and list[7] == a) or (
                list[2] == a and list[5] == a and list[8] == a) or (list[2] == a and list[4] == a and list[6] == a) or (
                list[3] == a and list[4] == a and list[5] == a) or (list[6] == a and list[7] == a and list[8] == a):
            print('\n' * 100)
            print_table(list)
            print('Player 1 wins.')
            break

        print('\n' * 100)
        print_table(list)
        player1_input(list, b)
        if (list[0] == b and list[1] == b and list[2] == b) or (list[0] == b and list[3] == b and list[6] == b) or (
                list[0] == b and list[4] == b and list[8] == b) or (list[1] == b and list[4] == b and list[7] == b) or (
                list[2] == b and list[5] == b and list[8] == b) or (list[2] == b and list[4] == b and list[6] == b) or (
                list[3] == b and list[4] == b and list[5] == b) or (list[6] == b and list[7] == b and list[8] == b):
            print('\n' * 100)
            print_table(list)
            print('Player 2 wins.')
            break


def player1_input(list, x):
    while True:
        position = int(input('Choose your next position: (1-9)\n'))
        if 10 <= position <= 0:
            print('Please choose one of the options below.')
        elif 10 > position > 0 and list[position - 1] == ' ':
            list[position - 1] = x
            break
        elif 10 > position > 0 and list[position - 1] != ' ':
            print('This field is used please choose another number.')


def print_table(table_list):
    print(f"   |      |   \n"
          f" {table_list[0]} |   {table_list[1]}  | {table_list[2]} \n"
          f"   |      |   \n"
          f"----------------\n"
          f"   |      |   \n"
          f" {table_list[3]} |   {table_list[4]}  | {table_list[5]} \n"
          f"   |      |   \n"
          f"----------------\n"
          f"   |      |   \n"
          f" {table_list[6]} |   {table_list[7]}  | {table_list[8]} \n"
          f"   |      |   \n")


def x_or_o():
    while True:
        answer = input('Player 1: Do you want to be X or O?\n')
        if answer.upper() == 'X':
            print('Player 1 will go first.')
            c = 'X'
            d = 'O'
            break
        elif answer.upper() == 'O':
            print('Player 1 will go first.')
            c = 'O'
            d = 'X'
            break
        else:
            print('Please enter X or O.')
    return [c, d]


def yes_or_no():
    while True:
        answer = input('Are you ready to play? Enter Yes or No.\n')
        if answer.upper() == 'YES':
            print("Let's get started")
            hey = True
            break
        elif answer.upper() == 'NO':
            print('Bye bye.')
            hey = False
            break
        else:
            print('Please enter Yes or No.')
    return hey


def replay():
    while True:
        answer = input('Do you want to play again? Enter Yes or No.\n')
        if answer.upper() == 'YES':
            hey = True
            break
        elif answer.upper() == 'NO':
            print('Bye bye.')
            hey = False
            break
        else:
            print('Please enter Yes or No.')
    return hey


play()
