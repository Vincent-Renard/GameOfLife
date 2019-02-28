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
