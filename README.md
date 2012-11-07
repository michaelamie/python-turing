# python-turing: A really, really simple Turing machine implemented in Python.

## Notes
Eventually, I would like to get around to adding some proper exception 
handling for errors and that sort of thing.

## Directions
Action tables are stored in an sqlite db in a table called "action" with the
following schema:
<table>
	<tr> <td>Field Name</td>	<td>Type</td> </tr>
	<tr> <td>state</td>			<td>TEXT</td> </tr>
	<tr> <td>symbol</td>		<td>TEXT</td> </tr>
	<tr> <td>state_new</td>		<td>TEXT</td> </tr>
	<tr> <td>symbol_new</td>	<td>TEXT</td> </tr>
	<tr> <td>action</td>		<td>TEXT</td> </tr>
</table>
For now, the starting state of the Turing machine tape can be declared as a
list argument when an instance of the Machine class is declared.

## Actions
The simulation expects the following strings in the action field:

- '>' Move tape head right
- '<' Move tape head left
