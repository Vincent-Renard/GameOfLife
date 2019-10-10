#! /usr/bin/env python3
# coding: utf-8
from Grid import Grid


class Game:
    _nb_generations = 0
    _grids = []
    _grid = ""

    def __init__(self, length, height, nb_generations):
        self._nb_generations = nb_generations
        self._grid = Grid(length, height)
        self._grids.append(self._grid)

    def run(self, path):
        self._grid.put_img(0, path)
        for i in range(1, self._nb_generations + 1):
            print("Génération", i)
            self._grid.gen_next_generation()
            self._grids.append(self._grid)
            self._grid.put_img(i, path)
