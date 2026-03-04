# pyright: strict
from string import ascii_uppercase
from core.common_types import Player

def make_players(players: type[Player]) -> list[PlayerData]:
    col = [PlayerData(player) for player in players]
    return col

class PlayerData:
    symbols_used: set[str] = set()
    def __init__(self, player: Player, display_symbol: str | None = None, display_name: str | None = None):
        self._player = player

        temp = display_symbol or ascii_uppercase[player.value - 1]
        if temp in PlayerData.symbols_used:
            raise ValueError
        self._symbol = temp
        PlayerData.symbols_used.add(temp)
        
        self.owned_tokens: set[tuple[int, int]] = set()
        self._display_name = display_name or f"Player {player.value}"
    
    @property
    def player(self) -> Player:
        return self._player

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def display_name(self) -> str:
        return self._display_name