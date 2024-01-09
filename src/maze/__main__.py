#!/usr/bin/env python3

import curses

from .board import Board
from .renderer import render
from .input import process_input


def main(stdscr) -> None:
    rows, columns = stdscr.getmaxyx()

    width = 50
    height = 50
    board = Board(width, height)
    board[1, 1] = 1

    while True:
        render(stdscr, board)
        process_input(stdscr, board)


curses.wrapper(main)
