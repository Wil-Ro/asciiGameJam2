#!/usr/bin/env python3

from .board import *

def process_input(screen, board: Board):
    key = screen.getch() # TODO check for kbhit
    if key == ord("q"):
        exit(0)

    if key == ord("w"):
        board.move_player((-1, 0))
    if key == ord("s"):
        board.move_player((1, 0))
    if key == ord("a"):
        board.move_player((0, -1))
    if key == ord("d"):
        board.move_player((0, 1))