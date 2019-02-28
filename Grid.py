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

    def get_lenght(self):
        return self._lenght

    def get_height(self):
        return self._height

    def put_img(self, n_generation, path):
        t = Image.fromarray(self._grid, 'RGB')
        t.save(path)
        pass

    def next_generation_cell(self, x, y):
        neighbooors = 0
        return neighbooors

    def gen_next_generation(self):
        pass
