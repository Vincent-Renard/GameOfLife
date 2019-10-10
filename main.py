#! /usr/bin/env python3
# coding: utf-8
from Game import Game
from Grid import Grid

if __name__ == '__main__':
    game = Game(2048, 2048, 100)
    game.run("res/")
