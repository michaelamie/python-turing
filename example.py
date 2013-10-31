#!/usr/bin/env python

from turing.data import TableData
from turing.machine import Machine
from turing.tape_view import TapeView


if __name__ == '__main__':

    # Set up the machine
    actionTable = TableData("example.db")
    tapeData = ['1', '1', '0', '1', '1', '0', '1', '0', '1', '1']
    tapePosition = 10
    tapeView = TapeView()
    
    # Create Turing machine instance
    machine = Machine(actionTable(), tapeData, tapePosition, tapeView)

    # Begin machine run loop
    machine.run()
