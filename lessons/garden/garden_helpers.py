"""Some functions for my garden plan!"""

__author__ = "730661559"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> dict[str, list[str]]:
    """Add plant under its kind."""
    if new_plant_kind in by_kind:
        by_kind[new_plant_kind].append(new_plant)
    else:
        by_kind[new_plant_kind] = [new_plant]
    return by_kind


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> dict[str, list[str]]:
    """Add plant under date to sow seeds."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = [plant]
    return garden_by_date


def lookup_by_kind_and_date(plants_by_kinds: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return string with list of plants if a specific kind to plant in a specific month."""
    if kind in plants_by_kinds and month in plants_by_date:
        kind_list = plants_by_kinds[kind]
        month_list = plants_by_date[month]
        combined_list = [plant for plant in kind_list if plant in month_list]
        if combined_list:
            return f"{kind}s to plant in {month}: {combined_list}."
    return f"NO {kind}s to plant in {month}."