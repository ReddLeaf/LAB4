from enum import Enum
from player import PlayerData
from common_types import WinConditionType, TokenPhysicsType, Player
from typing import Callable, Sequence
from abc import ABC, abstractmethod


# Win Conditions Part
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
    def is_game_done(self, grid: list[str], token: str) -> bool:
        pass

@load_wincon(WinConditionType.TIC_TAC_TOE)
class BasicTicTacToe(WinConditions):
    def is_game_done(self, grid: list[str], token: str) -> bool:
        for row in grid:
            counter = 0
            for col in row:
                if col == token:
                    counter += 1
                    if counter == 3:
                        return True
                else:
                    counter = 0

        for col in range(len(grid[0])):
            counter = 0 
            for row in grid:
                if row[col] == token:
                    counter += 1
                    if counter == 3:
                        return True
                else:
                    counter = 0
        
        return False

@load_wincon(WinConditionType.NOT_CONNECT_FOUR)
class NotConnectFour(WinConditions):
    ...

class TicTacTOe(WinConditions):
    ...


# Token Physics Part

_physics: dict[TokenPhysicsType, type[TokenPhysics]] = {}

def make_physics(phy_type: TokenPhysicsType) -> TokenPhysics:
    return _physics[phy_type]()

def load_physics(phy_type: TokenPhysicsType) -> Callable[[type[TokenPhysics]], type[TokenPhysics]]:
    def p_load(self:type[TokenPhysics]):
        _physics[phy_type] = self
        return self
    return p_load

class TokenPhysics(ABC):
    @abstractmethod
    def apply_physics(self, grid: list[list[str]], row: int, col: int) -> list[list[str]]:
        pass

@load_physics(TokenPhysicsType.FLOATING)
class Floating(TokenPhysics):
    def apply_physics(self, grid: list[list[str]], row: int, col: int) -> list[list[str]]:
        return grid