class Board:
    def __init__(self, size):
        """
        Create board class.
        Create grid using '.'.
        Place ship on board randomly.
        Set number of attempts to 5.
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

    def display(self):
        """Display the current state of the board."""
        for row in self.grid:
            print(" ".join(row))
        print()

while True:
    """
    User can create grid size.
    """
    user_size = input("Enter a number greater than or equal 2 to create grid.")
    try:
        user_size = int(user_size)
        if user_size < 2:
            raise ValueError("Grid size must be at least 2.")
        break  # Input is valid, exit the loop
    except ValueError:
        print("Invalid input. Please enter a number greater than or equal to 2.")