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

    def __str__(self):
        return '\t{' f'{self.val},' \
               f'{self.isLeaf},' \
               f'{self.topLeft},' \
               f'{self.topRight},' \
               f'{self.bottomLeft},' \
               f'{self.bottomRight}' '}'

    def __eq__(self, other):
        return self.val == other.val and \
            self.isLeaf == other.isLeaf and \
            self.topLeft == other.topLeft and \
            self.topRight == other.topRight and \
            self.bottomLeft == other.bottomLeft and \
            self.bottomRight == other.bottomRight


class Solution:
    grid: List[List[int]]
    n: int

    def construct(self, grid: List[List[int]]) -> Node:
        self.grid = grid
        self.n = len(grid) - 1
        return self.get_node_from_quad(0, 0, self.n, self.n)

    def get(self, x, y):
        return self.grid[x][y]

    def is_subgrid_equal(self, x0, y0, x1, y1) -> bool:
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if self.get(x0, y0) != self.get(x, y):
                    return False
        return True

    # Se todos os valores do grid na seção são iguais, gera um nó do tipo folha. Se não, gera os quatro filhos,
    # recursivamente.
    def get_node_from_quad(self, x0: int, y0: int, x1: int, y1: int) -> Node:
        # É uma folha se todos os valores da região forem iguais.
        is_leaf: bool = True
        # Valor do node é True se a grid for de 1's e False se for de 0's.

        # Caso Base 1: Grid com apenas um elemento.
        if y1 == y0 and x1 == x0:
            val = self.grid[x0][y0] == 1
            return Node(val=val, isLeaf=is_leaf,
                        topLeft=None,
                        bottomLeft=None,
                        topRight=None,
                        bottomRight=None)

        # Caso Base 2: Grid com todos os elementos iguais
        if self.is_subgrid_equal(x0, y0, x1, y1):
            val = (self.get(x0, y0) == 1)
            return Node(val=val, isLeaf=is_leaf, topLeft=None, bottomLeft=None, topRight=None, bottomRight=None)

        # Se não ocorre nenhum dos casos-base, dividir e conquistar.
        value = (self.get(x0, y1) == 1)
        x_mid = int((x0 + x1) / 2)
        y_mid = int((y0 + y1) / 2)

        top_lef = self.get_node_from_quad(x0, y0, x_mid, y_mid)
        top_rig = self.get_node_from_quad(x0, y_mid + 1, x_mid, y1)
        bot_lef = self.get_node_from_quad(x_mid + 1, y0, x1, y_mid)
        bot_rig = self.get_node_from_quad(x_mid + 1, y_mid + 1, x1, y1)

        return Node(value, False, top_lef, top_rig, bot_lef, bot_rig)
