from typing import List

from quad_tree import Solution, Node


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
        grid: List[List[int]] = [[0, 1],
                                 [1, 0]]
        out_tree: Node = Node(val=True,
                              isLeaf=False,
                              topLeft=self.leaf_grid_0,
                              topRight=self.leaf_grid_1,
                              bottomLeft=self.leaf_grid_1,
                              bottomRight=self.leaf_grid_0)
        assert self.sol.construct(grid).__eq__(out_tree)

    def test_grid_4by4(self):
        grid: List[List[int]] = [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [1, 1, 1, 1],
                                 [1, 1, 1, 1]]

        # Filhos do nível 1.
        tl_1 = self.leaf_grid_0
        tr_1 = self.leaf_grid_0
        bl_1 = self.leaf_grid_1
        br_1 = self.leaf_grid_1

        # Raiz
        out_tree = Node(False, False, tl_1, tr_1, bl_1, br_1)
        result = self.sol.construct(grid)
        assert result.__str__() == out_tree.__str__()
        assert result.__eq__(out_tree)

    def test_grid_8by8(self):
        grid: List[List[int]] = [[1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 0, 0, 0]]

        # Filhos do nível 2.
        tl_2 = self.leaf_grid_0
        tr_2 = self.leaf_grid_0
        bl_2 = self.leaf_grid_1
        br_2 = self.leaf_grid_1

        # Filhos do nível 1
        tl_1 = self.leaf_grid_1
        tr_1 = Node(False, False, tl_2, tr_2, bl_2, br_2)
        bl_1 = self.leaf_grid_1
        br_1 = self.leaf_grid_0

        # Raiz
        out_tree = Node(False, False, tl_1, tr_1, bl_1, br_1)
        result = self.sol.construct(grid)
        assert result.__str__() == out_tree.__str__()
        assert result.__eq__(out_tree)
