#!/usr/bin/env python3

import curses


def main(stdscr) -> None:
    rows, columns = stdscr.getmaxyx()

    stdscr.addstr(rows // 2, columns // 2, "x")
    stdscr.refresh()

    stdscr.addstr(rows // 2, columns // 2, str(stdscr.getch()))
    stdscr.getch()
    stdscr.refresh()


curses.wrapper(main)
