# pyright : strict

from core.common_types import WinConditionType, TokenPhysicsType, Player
from game.model import ConnectTacToeModel
from mechanics.token_physics import make_physics
from mechanics.win_conditions import make_wincon
from mechanics.player import PlayerData

def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    condition = make_wincon(win_condition_type)
    physics = make_physics(token_physics_type)
    players = [PlayerData(Player.P1, "X"), PlayerData(Player.P2, "O")]
    model = ConnectTacToeModel(players, condition, physics)
    return model