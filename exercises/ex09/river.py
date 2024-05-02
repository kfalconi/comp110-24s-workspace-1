"""File to define River class."""
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730661559"


class River:
    """Hi, this is the RIVER CLASS!"""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Fish and Bear age."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
    
    def remove_fish(self, amount: int):
        """Remove first fishes."""
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Bears are hungry."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Starve?"""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        
    def repopulate_fish(self):
        """Add fishes."""
        new_fish_count = (len(self.fish) // 2) * 4
        for k in range(new_fish_count):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Add bears."""
        new_bears_count = len(self.bears) // 2
        for k in range(new_bears_count):
            self.bears.append(Bear())
    
    def view_river(self):
        """View the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """7 times."""
        for k in range(7):
            self.one_river_day()