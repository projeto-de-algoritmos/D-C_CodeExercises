from typing import List


# Definition for a QuadTree node.

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    grid: List[List[int]]
    n: int

    def construct(self, grid: List[List[int]]) -> Node:
        self.grid = grid
        self.n = len(grid) - 1
        self.construct_recursive(0, self.n, 0, self.n)
        return None

    def get_node_from_quad(self, x0: int, x1: int, y0: int, y1: int) -> Node:
        top_left = self.grid[x1][y1]
        top_right = self.grid[x0][y1]
        bottom_left = self.grid[x0][y0]
        bottom_right = self.grid[x1][y0]

        print(f'top_left={top_left} top_right={top_right} bottom_left={bottom_left} bottom_right={bottom_right}')

        if bottom_right == bottom_left == top_left == top_right == 1:
            value = True
        elif bottom_right == bottom_left == top_left == top_right == 0:
            value = False
        else:
            raise Exception("Quad doesn't have equal values.")

        return Node(value, True, top_left, top_right, bottom_left, bottom_right)

    # x0, x1, y0, y1 -> x start, x end, y start, y end
    def construct_recursive(self, x0: int, x1: int, y0: int, y1: int) -> Node:
        # Base Case: all elements are equal
        # Base Case for recursion: matrix 1x1, i. e., y1 == y0 && x1 == x0
        #
        print(f'x = ({x0}, {x1}) and y = ({y0}, {y0})')
        print(f'dx = {x1 - x0}, dy = {y1 - y0} ')
        if y1 - y0 == 1 and x1 - x0 == 1:
            return self.get_node_from_quad(x0, x1, y0, y1)
        else:
            return None


grid: List[List[int]] = [[0, 1], [1, 0]]
quad_tree = Solution().construct(grid)
print(quad_tree)
