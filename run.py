import random

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

    def valid_guess(self, guess):
        """Check if the player's guess is valid."""
        if len(guess) != 2:
            return False
        row, col = guess
        return 0 <= row < self.size and 0 <= col < self.size

    def make_guess(self, row, col):
        """
        Process the player's guess and update the board.
        If the guess matches the ship's location, mark it as 'X' and return True.
        Otherwise, mark it as '0' and return False.
        """
        if (row, col) == self.ship:
            self.grid[row][col] = 'X'  
            return True
        else:
            self.grid[row][col] = '0'  
            return False

    def check_win(self):
        """Check if the ship has been sunk."""
        return self.grid[self.ship[0]][self.ship[1]] == 'X'

print("Welcome to the Battleship game made with python.")

while True:
    """
    User can create grid size.
    """
    user_size = input("Enter a number greater than or equal 2 to create grid.")
    try:
        user_size = int(user_size)
        if user_size < 2:
            raise ValueError("Grid size must be at least 2.")
        break  
    except ValueError:
        print("Invalid input. Please enter a number greater than or equal to 2.")

board = Board(user_size)

while board.attempts > 0:
    print("\nHere is the current board:")
    board.display()
    print(f"You have {board.attempts} attempts remaining.")

    user_input = input("Enter your guess as row,col (e.g., 1,2): ")
    try:
        guess = user_input.split(',')
        guess = (int(guess[0]), int(guess[1]))
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a comma.")
        continue

    if not board.valid_guess(guess):
        print("Invalid guess. Please try again.")
        continue

    row, col = guess
    if board.make_guess(row, col):
        print("Direct hit! You sunk my battleship!")
        break
    else:
        print("Miss!")
        if abs(row - board.ship[0]) <= 1 and abs(col - board.ship[1]) <= 1:
            print("Hint: You're really close!")

    board.attempts -= 1

if not board.check_win():
    print("You have run out of attempts! The ship was at:", board.ship)

replay = input("Would you like to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thank you for playing Battleship!")
            break