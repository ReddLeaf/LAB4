# pyright: strict

from collections.abc import Sequence
# pyright: strict
from typing import Sequence
from common_types import Player, WinConditionType, TokenPhysicsType

class ConnectTacToeModel:
    ROW_SIZE: int = 6
    COL_SIZE: int = 7

    def __init__(self, players: list[Player], condition: WinConditionType, token_type: TokenPhysicsType) -> None:
        self._turn = 0
        self._players = players
        self.condition = condition
        self.token_type = token_type
        self._display_token = ["O", "X"]
        self._grid = self._gen_map(self.ROW_SIZE, self.COL_SIZE)
        self._player_tokens: dict[Player, set[tuple[int, int]]] = {p : set() for p in players}
        self._winner = None

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
        if self._condition.test_cond():
            self._winner = self._players[self._turn - 1]
            return True
        return False

    @property
    def grids(self) -> list[str]:
        grid: list[str] = ["".join(row) for row in self._grid]
        return grid


    @property
    def row_count(self) -> int:
        return self.ROW_SIZE
    
    @property
    def col_count(self) -> int:
        return self.COL_SIZE

    def choose_cell(self, row: int, col: int) -> bool:        
        if not 0 <= row < self.ROW_SIZE:
            raise ValueError

        if not 0 <= col < self.COL_SIZE:
            raise ValueError

        if self.is_game_done:
            return False
        
        if self._grid[row][col] in {"."}:
            curr_player = self._players[self._turn]
            self._grid[row][col] = self._display_token[self._turn]
            self._player_tokens[curr_player].add((row, col))
            return True
        
        return False

    def advance_turn(self) -> None:
        self._turn += 1

    def get_owner(self, row: int, col: int) -> Player | None:
        for p in self._players:
            if (row, col) in self._player_tokens[p]:
                return p
        return None


class WinConditions:
    def is_game_done(self, grid: Sequence[list[str]], token: str) -> bool:
        ...

class BasicTicTacToe(WinConditions):
    def is_game_done(self, grid: Sequence[list[str]], token: str) -> bool:
        for row in grid:
            counter = 0
            for col in row:
                if col == token:
                    counter += 1
                    if counter == 3:
                        return True

        for col in range(len(grid[0])):
            counter = 0 
            for row in grid:
                if row[col] == token:
                    counter += 1
                    if counter == 3:
                        return True
        
        return False

class NotConnectFour(WinConditions):
    ...

class TicTacTOe(WinConditions):
    ...