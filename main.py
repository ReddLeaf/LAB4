from argparse import ArgumentParser
from model import ConnectTacToeModel
from view import ConntectTacToeView
from common_types import WinConditionType, TokenPhysicsType
from tester import make

if __name__ == '__main__':
    model = make(WinConditionType.TIC_TAC_TOE, TokenPhysicsType.FLOATING)
    view = ConnectTacToeView()
    control = ConnectTacToeControl()

    control.run()