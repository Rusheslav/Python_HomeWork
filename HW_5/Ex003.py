# Создайте программу для игры в ""Крестики-нолики""

from random import choice

def print_field(field: list) -> None:
    """
    Prints the current game field.
    :param field: game field.
    :return: does not return anything
    """
    print(f' {"а":^6}{"б":^6}{"в":^6}\n'
          ' -----------------\n'
          f'|{field[0]:^5}|{field[1]:^5}|{field[2]:^5}|{1:^5}\n'
          ' -----------------\n'
          f'|{field[3]:^5}|{field[4]:^5}|{field[5]:^5}|{2:^5}\n'
          ' -----------------\n'
          f'|{field[6]:^5}|{field[7]:^5}|{field[8]:^5}|{3:^5}\n'
          ' -----------------')


def check_winner(field: list, mark: str) -> bool:
    """
    Checks if there is a winner (i.e if there are three consecutive
    marks in one line, column or diagonal)
    :param field: game field
    :param mark: mark to be checked
    :return: boolean value
    """
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_combs:
        if field[comb[0]] == mark and field[comb[1]] == mark and field[comb[2]] == mark:
            return True
    return False


def check_draw(field: list) -> bool:
    """
    Checks if there is a draw (i.e. no possibility to make the next move)
    :param field: game field
    :return: boolean value
    """
    for i in field:
        if i == ' ':
            return False
    return True


def player_move(g_field: list, mark: str) -> None:
    """
    Working with the player's input to let him make the next move.
    :param g_field: game field
    :param mark: player's mark
    :return: doesn't return anything
    """
    print_field(g_field)
    moves_dict = {
        'а1': 0, 'б1': 1, 'в1': 2,
        'а2': 3, 'б2': 4, 'в2': 5,
        'а3': 6, 'б3': 7, 'в3': 8,
        '1а': 0, '1б': 1, '1в': 2,
        '2а': 3, '2б': 4, '2в': 5,
        '3а': 6, '3б': 7, '3в': 8,
        'a1': 0, 'a2': 3, 'a3': 6,        # Здесь английская "a"
        '1a': 0, '2a': 3, '3a': 6         # Здесь английская "a"
    }
    move = input(f'{player_name}, ваш ход (например, "а1"): ').lower()
    available_cells = [i for i in range(len(g_field)) if g_field[i] == ' ']
    while not (move in moves_dict.keys()):
        move = input('Ходы можно делать только в формате "{буква а, б или в}'
                     '{цифра}" (например, "а1"). Попробуйте ещё раз: ')
    while not moves_dict[move] in available_cells:
        move = input('Эта клетка занята. Попробуйте ещё раз: ')
    move = moves_dict[move]
    g_field[move] = mark


def get_win_move(field: list, mark_check: str, mark_put: str) -> bool:
    """
    Checks if one of the players can make a move to win the game
    (i.e. has two consequtive marks in one line, column or diagonal
    and a free cell in the same line, column or diagonal) and puts
    the required mark in that free cell to either win the game
    or prevent the second player from winning.
    :param field: game field
    :param mark_check: the mark to be checked
    :param mark_put: the mark to be put
    :return: boolean value
    """
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_combs:
        i, k, j = comb
        if field[i] == ' ' and field[k] == mark_check and field[j] == mark_check:
            field[i] = mark_put
            return True
        if field[j] == ' ' and field[i] == mark_check and field[k] == mark_check:
            field[j] = mark_put
            return True
        if field[k] == ' ' and field[j] == mark_check and field[i] == mark_check:
            field[k] = mark_put
            return True
    return False


def bot_move(g_field: list, mark: str, o_mark: str) -> None:
    """
    Letting the bot to make the next move
    :param g_field: game field
    :param mark: bot's mark
    :param o_mark: opponent's (player's) mark
    :return:
    """
    if get_win_move(g_field, mark, mark):
        return

    if get_win_move(g_field, o_mark, mark):
        return

    if g_field[4] == ' ':
        g_field[4] = mark
        return

    for k, v in {0: 8, 2: 6, 6: 2, 8: 0}.items():
        if g_field[k] == o_mark and g_field[v] == ' ':
            g_field[v] = mark
            return

    for i in (0, 2, 6, 8):
        if g_field[i] == ' ':
            g_field[i] = mark
            return

    for i in (1, 3, 5, 7):
        if g_field[i] == ' ':
            g_field[i] = mark
            return


game_field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_name = input('Введите ваше имя: ')

# Работа с вводом пользователя по выбору знака:
p_mark = input('Выберите знак (x/o): ')
while p_mark.lower() not in ['x', 'o', 'х', 'о', '0']:
    p_mark = input('Можно выбрать только буквы "x" и "o" или ноль ("0"): ')
if p_mark in 'xх':
    p_mark, b_mark = 'X', 'O'
else:
    p_mark, b_mark = 'O', 'X'

# Выбор начинающего и сам алгоритм игры (в циклах)
turn = choice([player_name, 'bot'])

if turn == player_name:
    while True:
        player_move(game_field, p_mark)
        if check_winner(game_field, p_mark):
            print_field(game_field)
            print(f'{player_name} победил!')
            break
        if check_draw(game_field):
            print_field(game_field)
            print(f'Ничья!')
            break
        bot_move(game_field, b_mark, p_mark)
        if check_winner(game_field, b_mark):
            print_field(game_field)
            print('Пластмассовый мир победил!')
            break
        if check_draw(game_field):
            print_field(game_field)
            print(f'Ничья!')
            break

else:
    while True:
        bot_move(game_field, b_mark, p_mark)
        if check_winner(game_field, b_mark):
            print_field(game_field)
            print('Пластмассовый мир победил!')
            break
        if check_draw(game_field):
            print_field(game_field)
            print(f'Ничья!')
            break
        player_move(game_field, p_mark)
        if check_winner(game_field, p_mark):
            print_field(game_field)
            print(f'{player_name} победил!')
            break
        if check_draw(game_field):
            print_field(game_field)
            print(f'Ничья!')
            break
