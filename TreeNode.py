class TreeNode:
  def __init__(self, parent, puzzle_state, cost):
    self.parent = parent
    self.puzzle_state = puzzle_state
    self.cost = cost

  def __lt__(self, other):
    return self.cost < other.cost