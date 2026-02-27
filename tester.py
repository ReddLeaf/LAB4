# pyright: strict

from common_types import WinConditionType, TokenPhysicsType
from model import ConnectTacToeModel


def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    ...