# pyright: strict

from collections.abc import Sequence
# pyright: strict
from typing import Sequence
from common_types import Player, TokenPhysicsType
from classes import WinConditions

class ConnectTacToeModel:
    ROW_SIZE: int = 6
    COL_SIZE: int = 7

    def __init__(self, players: list[Player], condition: WinConditions, token_type: TokenPhysicsType) -> None:
        self._turn: int = 0
        self._players = players
        self.condition = condition
        self.token_type = token_type
        self._display_token = ["O", "X"]
        self._grid = self._gen_map(self.ROW_SIZE, self.COL_SIZE)
        self._player_tokens: dict[Player, set[tuple[int, int]]] = {p : set() for p in players}
        self._winner = None
        self._is_game_done = False

    def _gen_map(self, row: int, col: int) -> Sequence[list[str]]:
        grid: list[list[str]] = [["." for _ in range(col)] for _ in range(row)]
        return grid

    @property
    def current_player(self) -> Player:
        num_players: int = len(self._players)
        return self._players[self._turn % num_players]

    @property
    def winner(self) -> Player | None:
        return self._winner

    @property
    def is_game_done(self) -> bool:
        return self._is_game_done

    @property
    def grid(self) -> list[str]:
        grid: list[str] = ["".join(row) for row in self._grid]
        return grid


    @property
    def row_count(self) -> int:
        return self.ROW_SIZE
    
    @property
    def col_count(self) -> int:
        return self.COL_SIZE

    def choose_cell(self, row: int, col: int) -> bool:        
        if 0 >= row or  row > self.ROW_SIZE+1:
            return False

        if 0 >= col or  col > self.COL_SIZE+1:
            return False

        if self.is_game_done:
            return False
        
        if self._grid[row][col] in {"."}:
            curr_player = self._players[self._turn]
            self._grid[row][col] = self._display_token[self._turn]
            self._player_tokens[curr_player].add((row, col))
            return True
        
        return False

    def advance_turn(self) -> None:
        self._is_game_done = self.condition.is_game_done(self.grid, self._display_token[self._turn])
        if self._is_game_done:
            self._winner = self._players[self._turn]
        self._turn = (self._turn + 1) % len(self._players)

    def get_owner(self, row: int, col: int) -> Player | None:
        for p in self._players:
            if (row, col) in self._player_tokens[p]:
                return p
        return None
