"""Practice writing a class."""

# Definition
class Profile:

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create a new class Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If Profile is public, print message."""
        if self.private is False:
            print(msg)
    
# Instantiation
user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool!")


