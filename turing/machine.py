import time
from tape import Tape


class Machine(object):
    
    def __init__(self, 
        data=None, tape_view=None, cells=[' '], position=1):

        self.tape = Tape(cells, position)
        self.states = {}
        self.state = u'0'
        self.view = tape_view
        
        assert data is not None, \
        "Action table data argument cannot be None"
        assert self.view is not None, \
        "Tape view argument cannot be None"
        
        for row in data:
            state = row[0]
            symbol = row[1]
            state_new = row[2]
            symbol_new = row[3]
            action = row[4]

            if self.states.get(state):
                self.states[state].update({
                    symbol: (state_new, symbol_new, action)
                })
            else:
                self.states[state] = {
                    symbol: (state_new, symbol_new, action)
                }
        

    def run(self, step_delay=1):
        self.view.update(self.tape.display_string(), 
                         self.tape.position, self.state)
        time.sleep(step_delay)
        while self.state != u'h':
            symbol = self.states.get(self.state).get(self.tape.get_symbol())
            if symbol != None:
                self.state = symbol[0]
                self.tape.write(symbol[1])
                if symbol[2] == u'>':
                    self.tape.right()
                elif symbol[2] == u'<':
                    self.tape.left()
            self.view.update(self.tape.display_string(), 
                             self.tape.position, self.state)
            time.sleep(step_delay)