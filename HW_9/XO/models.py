from random import shuffle
import user_interface as ui


player_mark = None
bot_mark = None


def get_marks():
    """Определяет начинающего игрока и распределяет символы"""

    global player_mark, bot_mark
    marks = [ui.X, ui.O]
    shuffle(marks)
    player_mark, bot_mark = marks
    return player_mark, bot_mark


def player_move(game_field: list, move: int) -> bool:
    """Обрабатывает ход игрока"""

    available_cells = [i for i in range(len(game_field)) if game_field[i] == ui.space]
    if move in available_cells and not check_winner(game_field, player_mark) and not check_winner(game_field, bot_mark):
        game_field[move] = player_mark
        return True
    return False


def check_draw(field: list) -> bool:
    """Проверяет позицию на игровом поле на ничью"""
    return ui.space not in field


def check_winner(field: list, mark: str) -> bool or tuple:
    """Проверяет позицию на поле на победу указанного символа"""
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_combs:
        if field[comb[0]] == mark and field[comb[1]] == mark and field[comb[2]] == mark:
            return comb
    return False


def bot_move(g_field: list, mark: str, o_mark: str) -> None:
    """Определяет ход бота"""

    if get_win_move(g_field, mark, mark):
        return

    if get_win_move(g_field, o_mark, mark):
        return

    if g_field[4] == ui.space:
        g_field[4] = mark
        ui.update_buttons()
        return

    for k, v in {0: 8, 2: 6, 6: 2, 8: 0}.items():
        if g_field[k] == o_mark and g_field[v] == ui.space:
            g_field[v] = mark
            return

    for i in (0, 2, 6, 8):
        if g_field[i] == ui.space:
            g_field[i] = mark
            return

    for i in (1, 3, 5, 7):
        if g_field[i] == ui.space:
            g_field[i] = mark
            return


def get_win_move(field: list, mark_check: str, mark_put: str) -> bool:
    """Проверяет, может ли один из игроков победить в игре следующим кодом"""
    win_combs = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_combs:
        i, k, j = comb
        if field[i] == ui.space and field[k] == mark_check and field[j] == mark_check:
            field[i] = mark_put
            return True
        if field[j] == ui.space and field[i] == mark_check and field[k] == mark_check:
            field[j] = mark_put
            return True
        if field[k] == ui.space and field[j] == mark_check and field[i] == mark_check:
            field[k] = mark_put
            return True
    return False
