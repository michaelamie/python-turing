#!/usr/bin/env python
from turing import *

machine = Machine( getdata('example.db'),
                   ['1', '1', '0', '1', '1', '0', '1', '0', '1', '1'],
                   10 )
view = TapeView()
machine.run(view)
del view
