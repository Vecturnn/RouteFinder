# Route Finder

## Project Description
This project aims to create a program that calculates the lowest cost route across a field with sinkholes. The program starts from the left side of the field and tries to reach the right side without stepping on sinkholes. The movement is restricted to horizontal and vertical directions only.

There are three types of movement costs depending on the proximity of sinkholes:
- **Cost1:** Moving to a cell with no sinkhole in any neighboring cell (including diagonals).
- **Cost2:** Moving to a cell with sinkholes in diagonal neighbors but none in horizontal or vertical neighbors.
- **Cost3:** Moving to a cell with sinkholes in horizontal or vertical neighbor cells.

The field is represented as a grid of cells where `0` indicates a sinkhole and `1` indicates ground.

## Input Format
- The first line contains the three costs (Cost1, Cost2, Cost3) separated by spaces.
- Following lines represent the field map with `0`s and `1`s separated by spaces.

## Output Format
- If no possible route exists, output:
There is no possible route!

- If at least one possible route exists, output:
Cost of the route: <COST_OF_THE_ROUTE>

Followed by a bird’s-eye view of the field with the route marked by `X`.

## Project Rules and Requirements
- The solution must use recursion appropriately.
- When searching for routes on the left side of the field, the uppermost cell should be tried first, then lower ones.
- When making a move, try neighbors in this order: right, up, down, left.
- The shortest route must be found and output. If multiple shortest routes exist, the first according to the above rules should be displayed.
- No global variables are allowed.
- The main function should serve only as a driver and not contain main logic.
- The code must be clean, readable, and properly commented (following PEP-8 and PEP-257 guidelines).
- The program must run on Python 3.9.18 at the department’s developer server (dev.cs.hacettepe.edu.tr).
- Output format must exactly match the specifications.
- Discussions on high-level design are allowed but sharing code or solutions is prohibited.

## How to Run
python3 route_finder.py input.txt output.txt

- `input.txt` contains the costs and map of the field.
- `output.txt` will contain the cost and the path or a no-route message.

## Example Input
1 2 3\n
1 1 0 1\n
1 1 1 0\n
0 1 1 1

## Example Output
Cost of the route: 7\n
X X 0 1\n
1 X X 0\n
0 1 X X

## Final Note: 
This project was a mandatory assignment as part of the BBM103: Introduction to Programming Laboratory I course at Hacettepe University. It was designed to provide practical experience in problem-solving and programming with recursion in Python.
