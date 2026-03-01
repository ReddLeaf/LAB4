from string import ascii_uppercase
from common_types import Player

def make_players(players: type[Player]) -> list[PlayerData]:
    col = [PlayerData(player) for player in players]
    return col

class PlayerData:
    count = 0 #Enum based or PlayerData based(?)
    def __init__(self, player: Player,  display_name: str | None = None):
        self._player = player
        self._symbol = ascii_uppercase[PlayerData.count]
        self.owned_tokens: set[tuple[int, int]] = set()
        self._display_name = display_name or f"Player {PlayerData.count + 1}"
        PlayerData.count = (PlayerData.count + 1) % 26
    
    #if needs be
    @classmethod
    def reset_count(cls):
        cls.count = 0

    @property
    def player(self) -> Player:
        return self._player

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def display_name(self) -> str:
        return self._display_name