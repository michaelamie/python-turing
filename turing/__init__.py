import sys, time, sqlite3, curses


class Tape(object):
  def __init__(self, cells=[], position=0):
    self.position = position
    self.cells = cells

  def length(self):
    return len(self.cells)

  def left(self):
    if self.position > 1:
      self.position -= 1
    else:
      self.cells.insert(0, None)

  def right(self):
    if self.position == self.length():
      self.cells.append(None)
    self.position += 1

  def write(self, symbol):
    if self.length() >= self.position:
      self.cells[self.position - 1] = symbol

  def displaystring(self):
    string = ('[')
    for cell in self.cells:
      string += '|'
      if cell == None:
        string += ' '
      else:
        string += cell.encode('ascii', 'ignore')
    string += '|]'
    return string

  def getsymbol(self):
    return self.cells[self.position - 1]


class Machine(object):
  def __init__(self, data, cells=[], position=0):
    self.tape = Tape(cells, position)
    self.states = {}
    self.state = u'0'
    for row in data:
      state = row[0]; symbol = row[1]; state_new = row[2];
      symbol_new = row[3]; action = row[4]
      if self.states.get(state):
        self.states[state].update({symbol:
                                   (state_new, symbol_new, action)})
      else:
        self.states[state] = {symbol: (state_new, symbol_new, action)}

  def run(self, view):
    view.update(self.tape.displaystring(), self.tape.position)
    time.sleep(1)
    while self.state != u'h':
      symbol = self.states.get(self.state).get(self.tape.getsymbol())
      if symbol != None:
        self.state = symbol[0]
        self.tape.write(symbol[1])
        if symbol[2] == u'>':
          self.tape.right()
        elif symbol[2] == u'<':
          self.tape.left()
      view.update(self.tape.displaystring(), self.tape.position)
      time.sleep(1)


class TapeView(object):
  def __init__(self):
    self.window = curses.initscr()
    curses.noecho()
    curses.curs_set(0)

  def __del__(self):
    self.window.addstr(2,0,'Simulation finished.\n  (enter to exit)')
    self.window.refresh()
    self.window.getch()
    curses.echo()
    curses.endwin()

  def update(self, string, new_position):
    self.window.clear()
    self.window.addstr(0,0, string)
    self.window.addch(1, new_position * 2, '^')
    self.window.refresh()


def getdata(filename):
  db = sqlite3.connect(filename)
  cursor = db.cursor()
  query = 'SELECT state, symbol, state_new, symbol_new, action'
  query += ' FROM action ORDER BY state'
  cursor.execute(query)
  data = []
  for row in cursor:
    data.append(row)
  cursor.close()
  db.close()
  return data
