#!/usr/bin/env python3

__all__ = (
    "render",
)

import curses

from .board import *

# TODO: Can we find nicer chars?
_CHARS = {
    EMPTY:  " ",
    WALL:   "#",
    PLAYER: "@",
    ENEMY:  "+",
}

_RADIUS = 10 # is const screaming snake case?
_DIMS = _RADIUS * 2 + 1


def calculate_offset(screen_dimensions, board_dimensions) -> tuple[int, int]:
    return (
        screen_dimensions[0] // 2 - board_dimensions[0] // 2,
        screen_dimensions[1] // 2 - board_dimensions[1] // 2,
    )


def render(screen , board: Board) -> None:
    rows, columns = screen.getmaxyx()

    view_x = min(board.width - _RADIUS - 1, max(_RADIUS, board.player_x))
    view_y = min(board.height - _RADIUS - 1, max(_RADIUS, board.player_y))

    subboard = board.get_surrounding_tile(_RADIUS, (view_x, view_y))
    origin_y, origin_x = calculate_offset((rows, columns), (_DIMS, _DIMS))

    # Rendering the board itself and the surrounding border.
    # ╭────────────────╮
    # │  woh cool box  │
    # ╰────────────────╯
    screen.addstr(origin_y - 1, origin_x - 1, "╭%s╮" % ("─" * _DIMS))
    for index, row in enumerate(subboard):
        screen.addstr(origin_y + index, origin_x - 1, "│%s│" % "".join(map(_CHARS.get, row)))
    screen.addstr(origin_y + len(subboard), origin_x - 1, "╰%s╯" % ("─" * _DIMS))

    # Render the player on top of the board so we don't have to deal with annoying tile manipulation stuff.
    screen.addstr(
        board.player_y - view_y + origin_y + _RADIUS,
        board.player_x - view_x + origin_x + _RADIUS,
        _CHARS[PLAYER],
    )

    screen.addstr(origin_y+len(subboard)+1, origin_x, f"x: {board.player_x} y: {board.player_y}      ")

    screen.refresh()
