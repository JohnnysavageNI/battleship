class Board:
    def __init__(self, size):
        """
        Create board class.
        Create grid using '.'.
        Place ship on board randomly.
        Set numbe rof attempts to 5.
        """
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ship = self.place_ship()
        self.attempts = 5