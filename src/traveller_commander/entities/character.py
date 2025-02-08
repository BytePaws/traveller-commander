"""
Models a player character.
"""

from entities import BaseEntity


class Character(BaseEntity):
    name: str

    def __init__(self, name: str):
        self.id = 1  # BUG Fix this
        self.name = name
        return self
