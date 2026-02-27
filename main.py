from argparse import ArgumentParser
from model import ConnectTacToeModel
from view import ConnectTacToeView:

if __name__ == '__main__':
    model = ConnectTacToeModel()
    view = ConnectTacToeView()
    control = ConnectTacToeControl()

    control.run()