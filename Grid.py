#! /usr/bin/env python3
# coding: utf-8
import numpy as np
from PIL import Image


class Grid:
    _lenght = 0
    _height = 0

    def __init__(self, lenght, height):
        self._height = height
        self._lenght = lenght
        self._grid = np.zeros((self._height, self._lenght, 3), dtype=np.uint8)

    def get_grid(self):
        return self._grid

    def put_img(self, n_generation, path):
        t = Image.fromarray(self._grid, 'RGB')
        t.save(path + "/gol[" + n_generation + "].png")

    def cell_is_alive(self, x, y):
        """

        :param x: coord x of the cell
        :param y: coord y of the cell
        :return: True if this cell is alive
        """
        return self._grid[x][y][0] == 0 and self._grid[x][y][1] == 0 and self._grid[x][y][2] == 0

    def next_generation_cell(self, x, y):
        """
        Generate the future cell
        :param x:
        :param y:
        :return:
        """
        neighbooors = self.get_neighbourhood(x, y)
        alive = [0, 0, 0]
        dead = [255, 255, 255]
        if self.cell_is_alive(x, y):
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
        grid_plus_un = np.zeros((self._height, self._lenght, 3), dtype=np.uint8)
        for l in range(self._lenght):
            for h in range(self._height):
                grid_plus_un[l][h] = self.next_generation_cell(l, h)

        pass

    def get_neighbourhood(self, i, j):
        voisins = 0

        return voisins
