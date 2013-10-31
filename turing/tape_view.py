import curses


class TapeView(object):

    def __init__(self, debug=False):
        self.debug = debug
        if not self.debug:
            self.window = curses.initscr()
            curses.noecho()
            curses.curs_set(0)

    def __del__(self):
        if not self.debug:
            self.window.addstr(2, 0, "Simulation finished.\n  (enter to exit)")
            self.window.refresh()
            self.window.getch()
            curses.echo()
            curses.endwin()

    def update(self, string, new_position, state):
        if not self.debug:
            self.window.clear()
            self.window.addstr(0, 0, string)
            self.window.addch(1, new_position * 2, '^')
            self.window.addstr(2, 0, "State: ")
            self.window.addch(2, 7, state.encode('ascii', 'ignore'))
            self.window.refresh()
        else:
            print string