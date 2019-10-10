#! /usr/bin/env python3
# coding: utf-8
import numpy as np
from PIL import Image
from random import randint


class Grid:
    _lenght = 0
    _height = 0

    def __init__(self, lenght, height):
        self._height = height
        self._lenght = lenght
        self._grid = np.zeros((self._height, self._lenght, 3), dtype=np.uint8)
        self._populate_first_grid()

    def _populate_first_grid(self):
        self._grid.fill(255)
        for l in range(self._lenght):
            for h in range(self._height):
                if randint(0, 1) == 1:
                    self._grid[h][l] = [0, 0, 0]

    def get_grid(self):
        return self._grid

    def put_img(self, n_generation, path):
        t = Image.fromarray(self._grid, 'RGB')
        t.save(path + "gol[" + str(n_generation) + "].png")

    def _cell_is_alive(self, c):
        return self._cell_is_alive_coord(c[1], c[0])

    def _cell_is_alive_coord(self, x, y):
        """
        Say whether cell[x,y] is alive
        :param x: coord x of the cell
        :param y: coord y of the cell
        :return: True if this cell is alive, False otherwise
        """
        return self._grid[x][y][0] == 0 and self._grid[x][y][1] == 0 and self._grid[x][y][2] == 0

    def _next_generation_cell(self, x, y):
        """
        Generate the future cell
        :param x: coord x of the cell
        :param y: coord y of the cell
        :return: Color of next cell
        """
        neighbooors = self._get_neighbourhood(x, y)
        alive = [0, 0, 0]
        dead = [255, 255, 255]
        if self._cell_is_alive_coord(x, y):
            if neighbooors < 2:
                return dead
            if neighbooors == 2 or neighbooors == 3:
                return alive
            if neighbooors > 3:
                return dead
        else:
            if neighbooors == 3:
                return alive
        return dead

    def gen_next_generation(self):
        """

        :return:
        """
        grid_next = np.zeros((self._height, self._lenght, 3), dtype=np.uint8)
        for l in range(self._lenght):
            for h in range(self._height):
                grid_next[h][l] = self._next_generation_cell(h, l)

        self._grid = grid_next

    def _get_neighbourhood(self, x, y):
        x, y = y, x
        """
            A B C
            D X E
            F G H
        :param x:
        :param y:
        :return: Number of neighbors
        """
        A = x - 1, y - 1
        B = x, y - 1
        C = x + 1, y - 1
        D = x - 1, y

        E = x + 1, y
        F = x - 1, y + 1
        G = x, y + 1
        H = x + 1, y + 1
        voisins = 0
        if x == 0 and y == 0:  # A
            # cas 3 voisins
            if self._cell_is_alive(E):
                voisins += 1
            if self._cell_is_alive(H):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1
        elif x == self._lenght - 1 and y == self._height - 1:  # H
            if self._cell_is_alive(A):
                voisins += 1
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(D):
                voisins += 1
        elif x == 0 and y == self._height - 1:  # F
            if self._cell_is_alive(C):
                voisins += 1
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(E):
                voisins += 1

        elif x == self._lenght - 1 and y == 0:  # C
            if self._cell_is_alive(F):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1
            if self._cell_is_alive(D):
                voisins += 1
        elif y == 0:  # B
            if self._cell_is_alive(D):
                voisins += 1
            if self._cell_is_alive(E):
                voisins += 1
            if self._cell_is_alive(F):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1
            if self._cell_is_alive(H):
                voisins += 1
        elif x == 0:  # D
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(C):
                voisins += 1
            if self._cell_is_alive(E):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1
            if self._cell_is_alive(H):
                voisins += 1

        elif x == self._lenght - 1:  # E
            if self._cell_is_alive(A):
                voisins += 1
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(D):
                voisins += 1
            if self._cell_is_alive(F):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1

        elif y == self._height - 1:  # G
            if self._cell_is_alive(A):
                voisins += 1
            if self._cell_is_alive(D):
                voisins += 1
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(C):
                voisins += 1
            if self._cell_is_alive(E):
                voisins += 1
        else:  # X
            if self._cell_is_alive(A):
                voisins += 1
            if self._cell_is_alive(B):
                voisins += 1
            if self._cell_is_alive(C):
                voisins += 1
            if self._cell_is_alive(D):
                voisins += 1
            if self._cell_is_alive(E):
                voisins += 1
            if self._cell_is_alive(F):
                voisins += 1
            if self._cell_is_alive(G):
                voisins += 1
            if self._cell_is_alive(H):
                voisins += 1

        return voisins
