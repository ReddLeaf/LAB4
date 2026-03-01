# pyright: strict
from core.common_types import WinConditionType, TokenPhysicsType
from tester import make
from game.view import ConnectTacToeView
from game.controller import ConnectTacToeController

if __name__ == '__main__':
    model = make(WinConditionType.TIC_TAC_TOE, TokenPhysicsType.FLOATING)
    view = ConnectTacToeView()
    control = ConnectTacToeController(view, model)
    
    control.run()