# pyright : strict

from common_types import WinConditionType, TokenPhysicsType, Player
from model import ConnectTacToeModel
from classes import NotConnectFour, BasicTicTacToe, make_wincon, make_physics,WinConditions, TokenPhysics

def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    condition = make_wincon(win_condition_type)
    physics = make_physics(token_physics_type)
    model = ConnectTacToeModel([Player.P1, Player.P2], condition, physics)
    return model