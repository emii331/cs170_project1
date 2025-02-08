
# built-in puzzles 
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
very_easy = [[1, 2, 3],
            [4, 5, 6],
            [0, 7, 8]]
easy = [[1, 2, 3],
       [5, 0, 6],
       [4, 7, 8]]
medium = [[1, 3, 6],
         [5, 0, 2],
         [4, 7, 8]]
hard = [[1, 6, 7],
       [5, 0, 3],
       [4, 8, 2]]
very_hard = [[0, 7, 2],
            [4, 6, 1],
            [3, 5, 8]]

def main():

  puzzle_type = input("Enter '1' to use a built-in puzzle or '2' to create your own:" + '\n')
  print("Selected mode: " + puzzle_type)

  if puzzle_type == "1":
    puzzle_to_solve = select_puzzle_difficulty()
  if puzzle_type == "2":
    puzzle_to_solve = create_puzzle()
  

  algorithm_choice = select_algorithm()

  if algorithm_choice == "1":
    uniform_cost_search(puzzle_to_solve, 0)
  if algorithm_choice == "2":
    uniform_cost_search(puzzle_to_solve, 1)

  return

def select_puzzle_difficulty():
  difficulty_choice = input("Please enter your choice of difficulty for the built-in puzzle on a scale from 0 - 5." + '\n')
  if difficulty_choice == "0":
    return trivial
  if difficulty_choice == "1":
    return very_easy
  if difficulty_choice == "2":
    return easy
  if difficulty_choice == "3":
    return medium
  if difficulty_choice == "4":
    return hard
  if difficulty_choice == "5":
    return very_hard

def create_puzzle():
  print("Please enter a valid 8-puzzle. Delimit numbers with a space, use 0 to represent the blank, and press enter after typing in each row." + '\n')
  row_one = input("Enter the first row: ")
  row_two = input("Enter the second row: ")
  row_three = input("Enter the third row: ")

  row_one = row_one.split()
  row_two = row_two.split()
  row_three = row_three.split()


  for i in range(0,3):
    row_one[i] = int(row_one[i])
    row_two[i] = int(row_two[i])
    row_three[i] = int(row_three[i])
  
  user_puzzle = [row_one, row_two, row_three]
  return user_puzzle

def select_algorithm():
  return input("Select an algorithm to solve the puzzle: '1' for Uniform Cost Search, '2' for Misplaced Tile Heuristic, or '3' for Manhattan Distance Heuristic" + '\n')

def uniform_cost_search(puzzle, heuristic):
  print("puzzle solved" + '\n')
  print_puzzle(puzzle)

def print_puzzle(puzzle):
  for i in range(0,3):
    print(puzzle[i])

  print('\n')

if __name__ == "__main__":
    main()
