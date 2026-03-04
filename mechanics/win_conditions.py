# pyright: strict
from typing import Callable
from abc import ABC, abstractmethod
from core.common_types import WinConditionType

_wincons: dict[WinConditionType, type[WinConditions]] = {}

def make_wincon(win_con: WinConditionType) -> WinConditions:
    return _wincons[win_con]()

def load_wincon(win_con:WinConditionType) -> Callable[[type[WinConditions]], type[WinConditions]]:
    def dec_load(self:type[WinConditions]):
        _wincons[win_con] = self
        return self
    return dec_load

class WinConditions(ABC):
    @abstractmethod
    def evaluate(self, grid: list[str], row: int, col: int) -> None | str:
        pass

# @load_wincon(WinConditionType.TIC_TAC_TOE)
# class BasicTicTacToe(WinConditions):
#     def is_game_done(self, grid: list[str], row: int, col: int) -> bool:
#         for row in grid:
#             counter = 0
#             for col in row:
#                 if col == token:
#                     counter += 1
#                     if counter == 3:
#                         return True
#                 else:
#                     counter = 0

#         for col in range(len(grid[0])):
#             counter = 0 
#             for row in grid:
#                 if row[col] == token:
#                     counter += 1
#                     if counter == 3:
#                         return True
#                 else:
#                     counter = 0
        
#         return False

@load_wincon(WinConditionType.NOT_CONNECT_FOUR)
class NotConnectFour(WinConditions):
    def evaluate(self, grid: list[str], row: int, col: int) ->  None | str:
        visited = [[False] * col for _ in range(row)]
        def dfs(r: int, c: int, letter: str) -> int: # i think recursive dfs is fine since 42 cells is well below recursion depth of 1k
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if visited[r][c]:
                return 0
            if grid[r][c] != letter:
                return 0
            
            visited[r][c] = True
            
            count = 1
            count += dfs(r+1, c, letter)
            count += dfs(r-1, c, letter)
            count += dfs(r, c+1, letter)
            count += dfs(r, c-1, letter)
            
            return count
        
        winners: set[str] = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] != "." and not visited[r][c]:
                    if dfs(r, c, grid[r][c]) >= 4:
                        winners.add(grid[r][c])

        has_valid_move = any("." in _row for _row in grid)

        if has_valid_move and not winners:
            return None

        if len(winners) == 1:
            return winners.pop()

        return "Draw"

@load_wincon(WinConditionType.TIC_TAC_TOE)
class TicTacTOe(WinConditions):
    def evaluate(self, grid: list[str], row: int, col: int) -> None | str:
        winners: set[str] = set()

        for r in range(row):
            token = grid[r][0]
            if token != "." and all(grid[r][c] == token for c in range(col)):
                winners.add(token)

        for c in range(col):
            token = grid[0][c]
            if token != "." and all(grid[r][c] == token for r in range(row)):
                winners.add(token)

        has_valid_move = any("." in _row for _row in grid)

        if has_valid_move and not winners:
            return None

        if len(winners) == 1:
            return winners.pop()

        return "Draw"