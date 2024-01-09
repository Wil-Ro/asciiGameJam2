#!/usr/bin/env python3

__all__ = (
    "EMPTY", "WALL", "PLAYER", "ENEMY",
    "Board",
)

import copy

# TODO: Could be an enum?
EMPTY  = 0
WALL   = 1
PLAYER = 2
ENEMY  = 3


class Board:
    """
    Internal indexing is y,x!!!!
    """

    __slots__ = ("width", "height", "_player_pos", "_contents")

    @property
    def player_x(self) -> int:
        return self._player_pos[0]

    @player_x.setter
    def player_x(self, value: int) -> None:
        if value < 0 or value >= self.width:
            return
        elif self._contents[value][self._player_pos[1]]:
            return
        self._player_pos[0] = value

    @property
    def player_y(self) -> int:
        return self._player_pos[1]

    @player_y.setter
    def player_y(self, value: int) -> None:
        if value < 0 or value >= self.height:
            return
        elif self._contents[self._player_pos[0]][value]:
            return
        self._player_pos[1] = value

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self._player_pos = [0, 0]

        self._contents: list[list[int]] = [[0 for y in range(height)] for x in range(width)]

    def __getitem__(self, item: tuple[int, int]) -> int:
        x, y = item
        if x < 0 or x > self.width or y < 0 or y > self.height:
            raise ValueError("Invalid tile coordinates %r" % item)
        return self._contents[y][x]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        x, y = key
        if x < 0 or x > self.width or y < 0 or y > self.height:
            raise ValueError("Invalid tile coordinates %r." % key)
        self._contents[y][x] = value

    # def get_tile(self, x: int, y: int) -> int:
    #     return self._contents[y][x]

    def get_surrounding_tile(self, radius: int, pos: tuple[int, int] | None = None) -> list[list[int]]:
        pos = pos or tuple(self._player_pos)
        bounds = (
            max(0, pos[0] - radius), min(self.width - 1, pos[0] + radius + 1),
            max(0, pos[1] - radius), min(self.height - 1, pos[1] + radius + 1),
        )

        surrounding = self._contents[bounds[2]: bounds[3]].copy()
        for index, row in enumerate(surrounding):
            surrounding[index] = row[bounds[0]: bounds[1]]

        return surrounding

    def set_contents(self, contents: list[list[int]]) -> None:
        if len(contents) != self.height or len(contents[0]) != self.width:
            raise ValueError("Contents width and/or height does not match.")
        self._contents = copy.deepcopy(contents)

    def move_player(self, delta: tuple[int, int]):
        self.player_y += delta[0]
        self.player_x += delta[1]