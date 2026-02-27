# pyright : strict

from common_types import WinconditionType, TokenPhysicsType, Player
from model import ConnectTacToeModel

def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    newmodel = ConnectTacToeModel([Player.P1,Player.P2],win_condition_type,token_physics_type)
    return model