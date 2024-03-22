"""Ex05 - Dictionary Utility Functions."""

__author__ = "730661559"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Keys of input become values and vice-versa."""
    inverted_dict = {}
    for key, in input in input.items():
        if input in inverted_dict:
            raise KeyError(f"Duplicate value {input} encountered.")
        inverted_dict[input] = key
    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns str for the color that appears most frequently."""
    common_color = {}
    for color in input.values():
        common_color[color] = common_color.get(color, 0) +1

    max = 0
    most_common = None
    for color, count in common_color.items():
        if count > max or (count == max and color.values().index(color) < color.values().index(most_common)):
            most_common = color
            max = count

    return most_common


def count(input: list[str]) -> dict[str, int]:
    """Each key is a unique value, and each value is the count of times it appeared."""
    result = {}
    for item in input:
        if item in result:
            result[item] +=1
        else:
            result[item] = 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Return the first letter of each word."""
    result = {}
    for word in input:
        first_letter = input[0].lower()
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]
    return result
    

def update_attendance(attendance_log, week_day, student):
    """"""
    if week_day in attendance_log:
        attendance_log[week_day].append(student)
    else:
        attendance_log[week_day] = [student]