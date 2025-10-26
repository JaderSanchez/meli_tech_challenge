import copy

def update_minesweeper_board(_board):

  # Break reference to avoid modify input value
  board = copy.deepcopy(_board)
  
  # Get rows and columns
  rows = len(board)
  cols = len(board[0]) if rows > 0 else 0

  # Validate board contains data
  if rows == 0 or cols == 0:
    raise ValueError("Board is empty.")

  # Validate board is well formed (each row contains the same number of cols)
  for i in range(rows):
    if len(board[i]) != cols:
      raise ValueError("Board columns are not equal in each row.")

  # Change 1 to 9 in board
  # And Validate board values
  for row in range(rows):
    for col in range(cols):

      # Verify all board values are 0 or 1
      if board[row][col] not in [0, 1]:
        raise ValueError("Board contains invalid values. Only 0 and 1 are allowed.")

      # Change value of mine position
      if board[row][col] == 1:
        board[row][col] = 9

  # Define adjacent positions
  adjacent_positions = [
    (-1, -1), # Top Left
    (-1, 0),  # Top
    (-1, 1),  # Top Right
    (0, 1),   # Right
    (1, 1),   # Bottom Right
    (1, 0),   # Bottom
    (1, -1),  # Bottom Left
    (0, -1),  # Left
  ]

  # Search for adjacent mines
  for row in range(rows):
    for col in range(cols):

      # Omit mines positions
      if board[row][col] == 9:
        continue

      # Init adjacent mines counter
      adjacent_mines = 0

      # For each position verify each adjacent position
      for adjacent_position in adjacent_positions:

        # Calculate adjacent position
        adjacent_row = row + adjacent_position[0]
        adjacent_col = col + adjacent_position[1]

        # Verify adjacent position is a valid into the board
        if adjacent_row >= 0 and adjacent_row <= rows - 1 and adjacent_col >= 0 and adjacent_col <= cols - 1:

          # Verify adjacent position is a mine
          if board[adjacent_row][adjacent_col] == 9:
            adjacent_mines += 1

      # Update position value with count of adjacent mines
      board[row][col] = adjacent_mines

  return board

# Test case
def main():

  input_board = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
  ]

  output_board = update_minesweeper_board(input_board)

  print('\n\nInput board\n')
  for row in input_board:
    print(row)

  print("\n\nOutput board\n")
  for row in output_board:
    print(row)

if __name__ == "__main__":
  main()