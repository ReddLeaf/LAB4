# pyright: strict
# from collections.abc import Sequence
from core.common_types import Player
from mechanics.token_physics import TokenPhysics
from mechanics.win_conditions import WinConditions
from mechanics.player import PlayerData

class ConnectTacToeModel:
    ROW_SIZE: int = 6
    COL_SIZE: int = 7

    def __init__(self, players: list[PlayerData], condition: WinConditions, token_type: TokenPhysics) -> None:
        self._players: list[PlayerData] = players
        self.condition: WinConditions = condition
        self.token_type: TokenPhysics = token_type

        self._grid: list[list[str]] = self._gen_map(self.ROW_SIZE, self.COL_SIZE)
        self._turn: int = 0
        self._winner = None
        self._is_game_done = False

        self._symbol_to_player: dict[str, PlayerData] = {p.symbol: p for p in self._players}

    def _gen_map(self, row: int, col: int) -> list[list[str]]:
        grid: list[list[str]] = [["." for _ in range(col)] for _ in range(row)]
        return grid

    @property
    def current_player(self) -> PlayerData:
        num_players: int = len(self._players)
        return self._players[self._turn % num_players]

    @property
    def winner(self) -> PlayerData | None:
        return self._winner

    @property
    def is_game_done(self) -> bool:
        return self._is_game_done

    @property
    def grid(self) -> list[str]:
        return ["".join(row) for row in self._grid]

    @property
    def row_count(self) -> int:
        return self.ROW_SIZE
    
    @property
    def col_count(self) -> int:
        return self.COL_SIZE

    def choose_cell(self, row: int, col: int) -> bool:        
        if not (0 <= row < self.row_count):
            return False

        if not (0 <= col < self.col_count):
            return False

        if self.is_game_done:
            return False
        
        if self._grid[row][col] in {"."}:
            curr_player = self.current_player
            self._grid[row][col] = curr_player.symbol
            curr_player.owned_tokens.add((row, col))
            return True
        
        return False

    def get_owner(self, row: int, col: int) -> Player | None:
        for p in self._players:
            if (row, col) in p.owned_tokens:
                return p.player
        return None

    def _evaluate_state(self):
        result= self.condition.evaluate(self.grid, self.row_count, self.col_count)

        if result is None:
            return

        self._winner = self._symbol_to_player.get(result, None) if result != "Draw" else None
        self._is_game_done = True

    def advance_turn(self) -> None:
        self._grid = self.token_type.apply_physics(self._grid, self.row_count, self.col_count)
        self._evaluate_state()
        self._turn = (self._turn + 1) % len(self._players)