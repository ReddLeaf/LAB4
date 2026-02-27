# pyright : strict

from model  import ConnectTacToeModel
from view import ConnectTacToeView


class ConnectTacToeController:

    def __init__(self,view:ConnectTacToeView,model:ConnectTacToeModel):
        self._view = view
        self._model = model

    def run(self):
        model = self._model
        view = self._view
        while not model.is_game_done:
            view.display_grid(model.grid)
            view.show_current_player(model.current_player)
            i,j = -1, -1
            while True:
                i,j = view.ask_for_ij(model.row_count,model.col_count)
                if model.choose_cell(i, j):
                    break
            model.advance_turn()
        view.show_winner(model.winner,model.grid)
        view.display_grid(model.grid)     