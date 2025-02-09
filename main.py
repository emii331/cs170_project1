from TreeNode import TreeNode
import heapq
import copy

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
goal_state = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]


def main():

  # Get user choice of built in or self-created puzzle, difficulty, and algorithm
  puzzle_type = input("Enter '1' to use a built-in puzzle or '2' to create your own:" + '\n')
  print("Selected mode: " + puzzle_type)

  if puzzle_type == "1":
    puzzle_to_solve = select_puzzle_difficulty()
  if puzzle_type == "2":
    puzzle_to_solve = create_puzzle()
  

  algorithm_choice = select_algorithm()

  # Call general search algorithm with the chosen puzzle and heuristic
  if algorithm_choice == "1":
    general_search(puzzle_to_solve, 1)
  if algorithm_choice == "2":
    general_search(puzzle_to_solve, 2)
  if algorithm_choice == "3":
    general_search(puzzle_to_solve, 3)

  return

# returns the puzzle corresponding to the inputed difficulty
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


# Asks for user input to create a puzzle
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


# Asks for user input to select algorithm to solve puzzle
def select_algorithm():
  return input("Select an algorithm to solve the puzzle: '1' for Uniform Cost Search, '2' for Misplaced Tile Heuristic, or '3' for Manhattan Distance Heuristic" + '\n')

# General search algorithm used for all three algorithms
def general_search(puzzle, heuristic):
  # Initialize variables and initial puzzle state
  initial_state = TreeNode(None, puzzle, 0, 0)
  initial_state.h_n = calc_cost(initial_state.puzzle_state, heuristic)
  nodes = []
  heapq.heappush(nodes, initial_state)
  max_queue_size = 0
  num_nodes_expanded = 0
  repeated_states = dict()
  puzzle_state_tree = []

  # loop while heap is not empty
  while len(nodes) > 0:
    max_queue_size = max(len(nodes), max_queue_size)
    if len(nodes) == 0:
      print("Failed to find goal state" + '\n')

    # pop minimum cost node from the heap
    node = heapq.heappop(nodes)
    if tuple(tuple(i) for i in node.puzzle_state) not in repeated_states:
      num_nodes_expanded += 1
      repeated_states[tuple(tuple(i) for i in node.puzzle_state)] = "Visited State"

    print("The best state to expand with a g(n) = " + str(node.g_n) + " and h(n) = " + str(node.h_n) + " is...\n")
    print_puzzle(node.puzzle_state)

    # check if popped node is the goal state
    if(node.puzzle_state == goal_state):
      print("Found goal state!\n")

      # print out solution path and solution properties
      print("Solution depth was " + str(node.g_n))
      print("Number of nodes expanded: " + str(num_nodes_expanded))
      print("Max queue size: " + str(max_queue_size) + '\n')

      print("Solution Path: ")
      node_on_solution_path = node
      solution_path = []

      while(node_on_solution_path != initial_state):
        solution_path.append(node_on_solution_path)
        node_on_solution_path = node_on_solution_path.parent
      solution_path.append(initial_state)

      for i in range(len(solution_path) - 1, -1, -1):
        print_puzzle(solution_path[i].puzzle_state)

      return
    

    # expand popped node, using the four operations (right, down, left, up)
    expansion = []

    zero_coords = find_zero_location(node.puzzle_state)
    if (zero_coords[1] < 2):
      coord_adjust = (0,1)
      new_puzzle_state = swap(node.puzzle_state, zero_coords, coord_adjust)
      move_right = TreeNode(node, new_puzzle_state, node.g_n + 1, calc_cost(new_puzzle_state, heuristic))
      expansion.append(move_right)
    if (zero_coords[0] < 2):
      coord_adjust = (1,0)
      new_puzzle_state = swap(node.puzzle_state, zero_coords, coord_adjust)
      move_down = TreeNode(node, new_puzzle_state, node.g_n + 1, calc_cost(new_puzzle_state, heuristic))
      expansion.append(move_down)    
    if (zero_coords[1] > 0):
      coord_adjust = (0,-1)
      new_puzzle_state = swap(node.puzzle_state, zero_coords, coord_adjust)
      move_left = TreeNode(node, new_puzzle_state, node.g_n + 1, calc_cost(new_puzzle_state, heuristic))
      expansion.append(move_left)   
    if (zero_coords[0] > 0):
      coord_adjust = (-1,0)
      new_puzzle_state = swap(node.puzzle_state, zero_coords, coord_adjust)
      move_up = TreeNode(node, new_puzzle_state, node.g_n + 1, calc_cost(new_puzzle_state, heuristic))
      expansion.append(move_up)


    for curr_neighbor in expansion:
      if tuple(tuple(i) for i in curr_neighbor.puzzle_state) not in repeated_states:
        heapq.heappush(nodes, curr_neighbor)
    
    expansion = []

  if len(nodes) == 0:
    print("Failed to find goal state" + '\n')

def find_zero_location(puzzle):
  for i in range(0,3):
    for j in range(0,3):
      if puzzle[i][j] == 0:
        return (i, j)
  return None

# gives new puzzle state according to how the zero tile is moved
def swap(puzzle, zero_coords, coord_adjust):
  new_puzzle = copy.deepcopy(puzzle)
  new_puzzle[zero_coords[0]][zero_coords[1]] = puzzle[zero_coords[0] + coord_adjust[0]][zero_coords[1] + coord_adjust[1]]
  new_puzzle[zero_coords[0] + coord_adjust[0]][zero_coords[1] + coord_adjust[1]] = 0

  return new_puzzle

# claculates the cost of the node according to the chosen heuristic
def calc_cost(puzzle, heuristic):
  if heuristic == 1:
    return 0
  
  if heuristic == 2:
    misplaced_tiles = 0
    for i in range(0,3):
      for j in range(0,3):
        if puzzle[i][j] != 0:
          if puzzle[i][j] != goal_state[i][j]:
            misplaced_tiles = misplaced_tiles + 1
    return misplaced_tiles
  
  if heuristic == 3:
                  #  0     1     2     3     4     5     6     7     8
    goal_coords = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
    manhattan_distance = 0
    for i in range(0,3):
      for j in range(0,3):
        if puzzle[i][j] != 0:
          x_distance = abs(i - goal_coords[puzzle[i][j]][0])
          y_distance = abs(j - goal_coords[puzzle[i][j]][1])
          manhattan_distance = manhattan_distance + x_distance + y_distance
    return manhattan_distance  


def print_puzzle(puzzle):
  for i in range(0,3):
    print(puzzle[i])

  print('\n')

if __name__ == "__main__":
    main()
