from common_types import WinConditionType, TokenPhysicsType
from typing import Callable, Sequence



class WinConditions:
    def is_game_done(self, grid: list[str], token: str) -> bool:
        ...

class TokenPhysics:
    def apply_physics(self, grid:Sequence[list[str]],row:int,col:int)->Sequence[list[str]]:
        ...

_wincons:dict[WinConditionType,type[WinConditions]] = {}

_physics:dict[TokenPhysicsType,type[TokenPhysics]] = {}

def load_wincon(win_con:WinConditionType)->Callable[[type[WinConditions]],type[WinConditions]]:
    def dec_load(self:type[WinConditions]):
        _wincons[win_con] = self
        return self
    return dec_load

def make_wincon(win_con:WinConditionType)->WinConditions:
    return _wincons[win_con]()


def load_physics(phy_type:TokenPhysicsType)->Callable[[type[TokenPhysics]],type[TokenPhysics]]:
    def p_load(self:type[TokenPhysics]):
        _physics[phy_type] = self
        return self
    return p_load

def make_physics(phy_type:TokenPhysicsType)->TokenPhysics:
    return _physics[phy_type]()


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

        for col in range(len(grid[0])):
            counter = 0 
            for row in grid:
                if row[col] == token:
                    counter += 1
                    if counter == 3:
                        return True
        
        return False

@load_wincon(WinConditionType.NOT_CONNECT_FOUR)
class NotConnectFour(WinConditions):
    ...

class TicTacTOe(WinConditions):
    ...


@load_physics(TokenPhysicsType.FLOATING)
class Floating(TokenPhysics):
    def apply_physics(self, grid:Sequence[list[str]],row:int,col:int)->Sequence[list[str]]:
        return grid