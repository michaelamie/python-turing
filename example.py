#!/usr/bin/env python

from turing.data import TableData
from turing.machine import Machine
from turing.tape_view import TapeView


if __name__ == '__main__':

    # Set up the machine
    action_table = TableData.load("example.db")
    tape_data = ['1', '1', '0', '1', '1', '0', '1', '0', '1', '1']
    tape_position = 10
    tape_view = TapeView()
   
    # Create Turing machine instance
    machine = Machine(action_table, tape_data, tape_position, tape_view)

    # Begin machine run loop
    machine.run(.5)
