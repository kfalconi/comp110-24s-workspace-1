"""Demonstrates range in a for loop."""

names: list[str] = ["Lele", "Erne", "foreverjuntos"]

for index in range(0, len(names)):
    print(f"{index}:{names[index]}")