"""
This module represents all items in the game.
"""

from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    type: str  # "weapon", "armor", "tool", etc
    price: int
    weight: float
    description: Optional[str] = None


class Weapon(Item):
    damage: str
    range: Optional[str] = None
    special: Optional[str] = None
