"""
Models all ship modules in the game.
"""

from pydantic import BaseModel, Field
from typing import Literal


class Hull(BaseModel):
    tonnage: int = Field(
        ..., description="Size of the Hull, measured in displacement tons (D-Tons)"
    )
    code: str = Field(..., description="Alphanumeric hull code")
    base_price: float = Field(..., description="Base price of this hull in MegaCredits")
    configuration: Literal["Standard", "Aerodynamic", "Segmented"] = "Standard"

    def get_total_price(self) -> float:
        """Calculates base price based on configuration."""
        if self.configuration == "Aerodynamic":
            return round(self.base_price * 1.1, 2)
        elif self.configuration == "Segmented":
            return round(self.base_price * 0.9, 2)
        return self.base_price

    def __str__(self):
        return f"{self.tonnage}T Hull (Code: {self.code}, Configuration: {self.configuration}, Price: {self.get_total_price()} MCr)"
