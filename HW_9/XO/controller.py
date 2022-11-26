import models as m
import user_interface as ui


def run():
    """Запускает основной цикл окна"""

    ui.xo.mainloop()


def start_game(name):
    """Запускает сеанс игры"""

    if name.strip():
        ui.update_dashboard(name)
        ui.update_buttons()
        player_mark, bot_mark = m.get_marks()
        if bot_mark == ui.X:
            m.bot_move(ui.game_field, ui.X, ui.O)


def get_move(move):
    """Обрабатывает ход игрока"""

    if ui.player_name and m.player_move(ui.game_field, move):
        ui.update_buttons()
        if win_combination := m.check_winner(ui.game_field, m.player_mark):
            ui.highlight_winner(m.player_mark, win_combination)
            ui.announce_winner(ui.player_name)
        elif m.check_draw(ui.game_field):
            ui.announce_winner('ничья')
        else:
            m.bot_move(ui.game_field, m.bot_mark, m.player_mark)
            ui.update_buttons()
            if win_combination := m.check_winner(ui.game_field, m.bot_mark):
                ui.highlight_winner(m.bot_mark, win_combination)
                ui.announce_winner()
            elif m.check_draw(ui.game_field):
                ui.announce_winner('ничья')
