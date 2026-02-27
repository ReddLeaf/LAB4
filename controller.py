# pyright : strict

from model  import ConnectTacToeModel
from view import ConnectTacToeViev


class ConnectTacToeController:

    def __init__(self,view:ConnectTacToeView,model:ConnectTacToeModel)
        self._view = view
        self._model = model

    def run(self):
        model = self._model
        view = self._view
        while not model.is_game_done:
            view.display_grid()
            view.show_current_player(model.current_player)
            i,j = float('inf'), float('inf')
            while not choose_cell(i,j):
                i,j = view.ask_for_ij(model.row_count,model.col_count)
            model.advance_turn()
        view.show_winner(model.winner)
        