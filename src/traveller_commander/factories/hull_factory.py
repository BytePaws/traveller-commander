import json
from pathlib import Path
from traveller_commander.entities.ship import Hull

DATA_PATH = Path(__file__).parent.parent / "data" / "hulls.json"


def load_hulls():
    "Loads all ship hulls from the JSON and returns them as list of Hull objects."
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return [Hull(**hull) for hull in data]


def get_hull_by_tonnage(tonnage: int, configuration: str = "Standard") -> Hull:
    """Searches for a hull by tonnage and applies the given configuration."""
    hulls = load_hulls()
    for hull in hulls:
        if hull.tonnage == tonnage:
            return Hull(**hull.dict(), configuration=configuration)
    raise ValueError(f"No Hull of {tonnage} tons found!")
