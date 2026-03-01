from typing import Callable
from abc import ABC, abstractmethod
from core.common_types import TokenPhysicsType

_physics: dict[TokenPhysicsType, type[TokenPhysics]] = {}

def make_physics(phy_type: TokenPhysicsType) -> TokenPhysics:   
    return _physics[phy_type]()

def load_physics(phy_type: TokenPhysicsType) -> Callable[[type[TokenPhysics]], type[TokenPhysics]]:
    def p_load(self:type[TokenPhysics]):
        _physics[phy_type] = self
        return self
    return p_load

class TokenPhysics(ABC):
    @abstractmethod
    def apply_physics(self, grid: list[list[str]], row: int, col: int) -> list[list[str]]:
        pass

@load_physics(TokenPhysicsType.FLOATING)
class Floating(TokenPhysics):
    def apply_physics(self, grid: list[list[str]], row: int, col: int) -> list[list[str]]:
        return grid