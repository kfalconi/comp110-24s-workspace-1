"""Test my garden functions."""

__author__ = "730661559"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind()-> None:
    """Use Case - Add plant by kind."""
    test_dict: dict[str, list[str]] = {"flower": ["rose", "tulip"]}
    plant_kind: str = "flower"
    plant: str = "sunflower"
    expected_dict: dict[str, list[str]] = {"flower": ["rose", "tulip", "sunflower"]}
    assert add_by_kind(test_dict, plant_kind, plant) == expected_dict


def test_add_plant_kind_none() -> None:
    """Edge Case - No chnage because empty plant shouldn't add."""
    test_dict: dict[str, list[str]] = {"flower": ["rose", "tulip"]}
    plant_kind: str = "flower"
    plant: str = ""
    expected_dict: dict[str, list[str]] = {"flower": ["rose", "tulip"]}
    assert add_by_kind(test_dict, plant_kind, plant) == expected_dict


def test_add_by_date() -> None:
    """Use Case - Add plant by month."""
    test_dict: dict[str, list[str]] = {"november": []}
    month: str = "november"
    plant: str = "celery"
    expected_dict: dict[str, list[str]] = {"november": ["celery"]}
    assert add_by_date(test_dict, month, plant) == expected_dict


def test_add_by_date_none() -> None:
    """Edge Case - No change because empty plant doesn't add."""
    test_dict: dict[str, list[str]] = {"november": ["rose"]}
    month: str = "november"
    plant: str = ""
    expected_dict: dict[str, list[str]] = {"november": ["rose"]}
    assert add_by_date(test_dict, month, plant) == expected_dict


def test_lookup_by_kind_and_date() -> None:
    """Return: str with list[plants of a specific kind, in a determined month]."""
    test_by_kind: dict[str, list[str]] = {"flower": ["rose", "tulip"]}
    test_by_date: dict[str, list[str]] = {"november": ["rose"]}
    month: str = "november"
    plant: str = "flower"
    expected_result: str = "flower to plant in november ['rose']"
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, month, plant) == expected_result


def test_no_date() -> None:
    """Return: str with list[plants of a specific kind]."""
    test_by_kind: dict[str, list[str]] = {"flower": ["rose", "tulip"], "vegetable": ["carrot"]}
    test_by_date: dict[str, list[str]] = {"november": ["rose"]}
    month: str = "november"
    plant: str = "vegetable"
    expected_result: str = "No vegetable in november."
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, month, plant) == expected_result