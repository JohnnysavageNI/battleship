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

    def place_ship(self):
        """
        Position ship on the board
        """
        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        return (row, col)