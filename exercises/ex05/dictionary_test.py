"""EX05 - Dict Unit Test!"""

__author__ = "730661559"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Invert
def test_invert_empty_dict() -> None:
    """Edge - empty input dict -> new empty dict."""
    assert invert([]) == {} 


def test_single_input() -> None: 
    """Use - test a function that only has one input pair."""
    test_dict: dict[str, str] = {"Kare": "November"}
    assert invert(test_dict) == {"November": "Kare"}


def test_multiple_input() -> None:
    """Use - test a function that has multiple input pairs."""
    test_dict: dict[str, str] = {"Kare": "November", "Lele": "January", "Cris": "September"}
    assert invert(test_dict) == {"November": "Kare", "January": "Lele", "September": "Cris"}


# Favorite_color
def test_favorite_color_empty_dict() -> None:
    """Edge - input empty dict -> empty string."""
    assert favorite_color([]) == ""


def test_tie() -> None:
    """Use - link favorite color -> first color that appeared."""
    test_dict: dict[str, str] = {"Kare": "Pink", "Lele": "Blue"}
    assert favorite_color(test_dict) == "Pink"


def test_multiple_people_single_color() -> None:
    """Use - many names linked with the same color -> pink once."""
    test_dict: dict[str, str] = {"Kare": "Pink", "Lele": "Pink", "Cris": "Pink"}
    assert favorite_color(test_dict) == "Pink"


# Count
def test_empty_list() -> None:
    """Edge - input empty list -> an empty dict."""
    assert count([]) == {}


def test_unique_inputs() -> None:
    """Use - testing a function that has many unique inputs."""
    test_list: list[str] = ["Pink", "Blue", "Red", "Purple"]
    assert count(test_list) == {"Pink": 1, "Blue": 1, "Red": 1, "Purple": 1}


def test_same_inputs() -> None:
    """Use - testing a function containing equal inputs."""
    test_list: list[str] = ["Pink", "Pink", "Pink", "Blue", "Blue"]
    assert count(test_list) == {"Pink": 3, "Blue": 2}


# Alphabetizer
def test_alphabetizer_empty_list() -> None:
    """Edge - input empty list -> empty Dict."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_duplicate_inputs() -> None:
    """Use - test a function containing duplicate inputs."""
    test_list: list[str] = ["cat", "cat", "dog"]
    assert alphabetizer(test_list) == {"c": ["cat", "cat"], "d": ["dog"]}


def test_case_sensitive_input() -> None:
    """Use case - testing if function is case sensitive."""
    """Use - testing if the function also works with upper and lower case letters."""
    test_list: list[str] = ["cat", "Cat", "dog", "Dog"]
    assert alphabetizer(test_list) == {"c": ["cat", "Cat"], "d": ["dog", "Dog"]}


# Update_attendance
def test_update_attendance_empty_dict() -> None:
    """Edge - empty Dict -> empty Dict."""
    test_dict: dict[str, list[str]] = {}
    day: str = "Tuesday"
    name: str = "Kare"
    assert update_attendance(test_dict, day, name) == {"Tuesday": ["Kare"]}


def test_add_name_existing_day() -> None:
    """Edge - testing the function when adding another name to an established day."""
    test_dict: dict[str, list[str]] = {"Tuesday": ["Kare"]}
    day: str = "Tuesday"
    name: str = "Lele"
    assert update_attendance(test_dict, day, name) == {"Tuesday": ["Kare", "Lele"]}


def test_add_existing_name_new_day() -> None:
    """Edge - testing a function when adding an established name to another day."""
    test_dict: dict[str, list[str]] = {"Tuesday": ["Kare", "Lele"]}
    day: str = "Sunday"
    name: str = "Lele"
    assert update_attendance(test_dict, day, name) == {"Tuesday": ["Kare", "Lele"], "Sunday": ["Lele"]}