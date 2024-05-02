"""River simulation defining Main."""
from exercises.ex09.river import River

__author__ = "730661559"


def main():
    """Defining the main."""
    my_river = River(num_fish=10, num_bear=2)

    my_river.view_river()

    my_river.one_river_day()

    my_river.view_river()

    my_river.one_river_week()

    my_river.view_river()


if __name__ == "__main__":
    main()