import sys
from typing import List

import pytest

from quad_tree import Solution, Node

grid8: List[List[int]] = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]


class TestSolution:
    sol: Solution = Solution()
    leaf_grid_1: Node = Node(True, True, None, None, None, None)
    leaf_grid_0: Node = Node(False, True, None, None, None, None)

    def test_grid_1(self):
        grid: List[List[int]] = [[1]]
        assert self.sol.construct(grid).__eq__(self.leaf_grid_1)

    def test_grid_1_with_0(self):
        grid: List[List[int]] = [[0]]
        assert self.sol.construct(grid).__eq__(self.leaf_grid_0)

    def test_grid_2_full_with_0(self):
        grid: List[List[int]] = [[0, 0], [0, 0]]
        assert self.sol.construct(grid).__eq__(self.leaf_grid_0)

    def test_grid_2_full_with_1(self):
        grid: List[List[int]] = [[1, 1], [1, 1]]
        assert self.sol.construct(grid).__eq__(self.leaf_grid_1)

    def test_grid_generating_one_node(self):
        grid: List[List[int]] = [[1, 2],
                                 [3, 4]]
        out_tree: Node = Node(val=True,
                              isLeaf=False,
                              topLeft=self.leaf_grid_0,
                              topRight=self.leaf_grid_1,
                              bottomLeft=self.leaf_grid_1,
                              bottomRight=self.leaf_grid_0)
        assert self.sol.construct(grid).__eq__(out_tree)

    def test_print_grid(self):
        grid: List[List[int]] = [[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12],
                                 [13, 14, 15, 16]]
        out_tree: Node = Node(val=True,
                              isLeaf=False,
                              topLeft=self.leaf_grid_0,
                              topRight=self.leaf_grid_1,
                              bottomLeft=self.leaf_grid_1,
                              bottomRight=self.leaf_grid_0)
        assert self.sol.construct(grid).__eq__(out_tree)
