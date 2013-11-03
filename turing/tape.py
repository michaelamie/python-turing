class Tape(object):

    def __init__(self, cells=[None], position=1):
        self.cells = cells
        self.position = position

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

    def display_string(self):
        string = ('[')
        for cell in self.cells:
            string += '|'
            if cell == None:
                string += ' '
            else:
                string += cell.encode('ascii', 'ignore')
        string += '|]'
        return string

    def get_symbol(self):
        return self.cells[self.position - 1]