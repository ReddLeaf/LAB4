# pyright : strict

from common_types import WinConditionType, TokenPhysicsType, Player
from model import ConnectTacToeModel, NotConnectFour, WinConditions, BasicTicTacToe


def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    condition: WinConditions
    if win_condition_type == WinConditionType.NOT_CONNECT_FOUR:
        condition = NotConnectFour()
    elif win_condition_type == WinConditionType.TIC_TAC_TOE:
        condition = BasicTicTacToe()

    model = ConnectTacToeModel([Player.P1, Player.P2], condition, token_physics_type)
    return model