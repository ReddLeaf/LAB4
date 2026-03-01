# pyright : strict

from common_types import WinConditionType, TokenPhysicsType, Player
from model import ConnectTacToeModel
from classes import NotConnectFour, BasicTicTacToe, make_wincon, make_physics,WinConditions, TokenPhysics
from player import PlayerData, make_players

def make(win_condition_type: WinConditionType, token_physics_type: TokenPhysicsType) -> ConnectTacToeModel:
    condition = make_wincon(win_condition_type)
    physics = make_physics(token_physics_type)
    players = make_players(Player)
    model = ConnectTacToeModel(players, condition, physics)
    return model