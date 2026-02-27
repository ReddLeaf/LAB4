# pyright: strict

from common_types import Player

class ConnectTacToeView:
    def display_grid(self, grid:  list[str]):
        print("  ".join(row) for row in grid)
        print()

    def ask_for_ij(self, rows: int, cols: int) -> tuple[int, int]:
        i, j = -1, -1

        while not 0 <= i < rows:
            try:
                i = int(input(f"Choose a row    [1-{rows}]: ")) - 1
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print("Invalid row! Please try again.")

        while not 0 <= j < cols:
            try:
                j = int(input(f"Choose a column [1-{cols}]: ")) - 1
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print("Invalid column! Please try again.")

        print()
        return (i, j)
    
    def show_current_player(self, player: Player):
        print(f"Player {player}'s turn")

    def show_winner(self, winner: Player):
        print()
