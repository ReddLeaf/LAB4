class WinConditions:
    def is_game_done(self, grid: list[str], token: str) -> bool:
        ...

class BasicTicTacToe(WinConditions):
    def is_game_done(self, grid: list[str], token: str) -> bool:
        for row in grid:
            counter = 0
            for col in row:
                if col == token:
                    counter += 1
                    if counter == 3:
                        return True

        for col in range(len(grid[0])):
            counter = 0 
            for row in grid:
                if row[col] == token:
                    counter += 1
                    if counter == 3:
                        return True
        
        return False

class NotConnectFour(WinConditions):
    ...

class TicTacTOe(WinConditions):
    ...