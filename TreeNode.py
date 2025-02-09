class TreeNode:
  def __init__(self, parent, puzzle_state, g_n, h_n):
    self.parent = parent
    self.puzzle_state = puzzle_state
    self.g_n = g_n
    self.h_n = h_n

  def __lt__(self, other):
    return (self.g_n + self.h_n) < (other.g_n + other.h_n)