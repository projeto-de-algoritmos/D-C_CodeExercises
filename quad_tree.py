import math
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
        # return '\n{' f'val = {self.val},' \
        #        f'isLeaf = {self.isLeaf},' \
        #        f'topLeft = {self.topLeft},' \
        #        f'topRight = {self.topRight},' \
        #        f'bottomLeft = {self.bottomLeft},' \
        #        f'bottomRight = {self.bottomRight}' '}'

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

    def print_subgrid(self, x0, y0, x1, y1):
        for row in self.grid[x0:x1 + 1]:
            print(row[y0:y1 + 1])

    # Se todos os valores do grid na seção são iguais, gera um nó do tipo folha. Se não, gera os quatro filhos,

    # recursivamente.
    def get_node_from_quad(self, x0: int, y0: int, x1: int, y1: int) -> Node:
        # É uma folha se todos os valores da região forem iguais.
        isLeaf: bool = True
        # Valor do node é True se a grid for de 1's e False se for de 0's.
        value: bool = True

        # Caso Base 1: Grid com apenas um elemento.
        if y1 == y0 and x1 == x0:
            val = self.grid[x0][y0] == 1
            return Node(val=val, isLeaf=isLeaf,
                        topLeft=None,
                        bottomLeft=None,
                        topRight=None,
                        bottomRight=None)

        # Caso Base 2: Grid com todos os elementos iguais
        el_sum = 0
        max_sum = 0

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                max_sum += 1
                el_sum += self.grid[i][j]

        if el_sum == max_sum:
            return Node(val=True, isLeaf=isLeaf, topLeft=None, bottomLeft=None, topRight=None, bottomRight=None)
        if el_sum == 0:
            return Node(val=False, isLeaf=isLeaf, topLeft=None, bottomLeft=None, topRight=None, bottomRight=None)

        # Se não ocorre nenhum dos casos-base, dividir e conquistar.
        top_rig = self.get(x0, y1)

        if top_rig == 0:
            value = False
        x_mid = math.floor((x0 + x1) / 2)
        y_mid = math.floor((y0 + y1) / 2)

        top_lef = self.get_node_from_quad(x0, y0, x_mid, y_mid)
        top_rig = self.get_node_from_quad(x0, y_mid + 1, x_mid, y1)
        bot_lef = self.get_node_from_quad(x_mid + 1, y0, x1, y_mid)
        bot_rig = self.get_node_from_quad(x_mid + 1, y_mid + 1, x1, y1)

        node = Node(value, False, top_lef, top_rig, bot_lef, bot_rig)
        return node
