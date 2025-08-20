import sys

def main():
    with open(sys.argv[1], "r") as infile:
        input = infile.read()
        cost1 = int(input.split("\n", maxsplit=1)[0].split()[0])
        cost2 = int(input.split("\n", maxsplit=1)[0].split()[1])
        cost3 = int(input.split("\n", maxsplit=1)[0].split()[2])
        costs = (cost1, cost2, cost3)
        input_table = input.split("\n", maxsplit=1)[1].strip()
    
    grid = cell_db(input_table)
    starting_positions = starting_position(grid) # All possible starting positions
    starting_point_results = [[[], float("inf")]] # For the first cell, max cost will be determined as infinity
    def route_cost(routeinfo):
        return routeinfo[1]

    for position in starting_positions:
        current_cost = calculate_cost([position[0],position[1]],costs,grid)
        starting_point_results.append(nextstep(costs, position, [], 0, grid, min(starting_point_results, key=route_cost)[1]))
    result = min(starting_point_results, key=lambda x: x[1]) # out of all results, select the path that has lowest cost

    f = open(sys.argv[2], "w")
    if result[1] == float("inf"):
        f.write("There is no possible route!")
    else:
        f.write(f"Cost of the route: {result[1]}")
        drawpath(result[0], grid, f)

def cell_db(table): # creates a list that contains every row and column data: [[row0],[row1],[cell0,cell1,cell2...]
        celldb = []
        introw = []
        for row in table.strip().split("\n"):
            strrow = row.split(" ") # makes every column in rows different element but in a string type
            for cell in strrow:
                introw.append(int(cell))
            celldb.append(introw) # makes every cell data integer and adds them to cell list
            introw = []
        return celldb

def cell(x,y,db): # Returns the cell in related position
    try:
        if x < 0 or y < 0:
            raise IndexError
        return db[y][x]
    except IndexError:
        return -1 # "-1" stands for "Outside of the grid"

def starting_position(grid): # creates a list that contains "1" cell that are in the first column
    starting_pos = []
    for i in range(len(grid)):
        if cell(0,i,grid) == 1:
            starting_pos.append([0,i])
    return starting_pos

def calculate_cost(position, costs, grid): # calculates the cost of the corresponding cell
    x = position[0]
    y = position[1]
    if cell(x+1,y,grid) == 0 or cell(x-1,y,grid) == 0 or cell(x,y-1,grid) == 0 or cell(x,y+1,grid) == 0: # checks if there is at least one "0" next to the main cell
        return costs[2]
    elif cell(x+1,y+1,grid) == 0 or cell(x-1,y+1,grid) == 0 or cell(x+1,y-1,grid) == 0 or cell(x-1,y-1,grid) == 0: # checks if there is at least one "0" on the diagonal
        return costs[1]
    else: # if there is no "0" around the main cell
        return costs[0]

def nextstep(costs, position, visited_cells, current_cost, grid, maxcost): # expected return format is: [visited_cells, maxcost]
    # Add the cost of current cell
    current_cost += calculate_cost(position, costs, grid)

    # check if we visited this cell before or is this cell is 0 or did we reach max cost
    if position in visited_cells or current_cost >= maxcost or cell(position[0],position[1],grid) == 0 or cell(position[0],position[1],grid) == -1:
        return ([], float("inf")) # to prevent of selection of this path, the current_cost will be determined as infinity for this cell

    visited_cells.append(position)

    if position[0] == len(grid[0])-1: # check if we reached to the end
        return (visited_cells, current_cost)
    
    # to keep every track seperately, visited_cells are copied
    up_visited_cells, down_visited_cells, left_visited_cells = (visited_cells.copy(), visited_cells.copy(), visited_cells.copy())

    # from the current cell; right, up, down and left cells will be selected to go, respectively.
    right_visited_cells, right_maxcost = nextstep(costs, [position[0]+1,position[1]], visited_cells, current_cost, grid, maxcost)

    if position[1]-1 >= 0:
        up_visited_cells, up_maxcost = nextstep(costs, [position[0],position[1]-1], up_visited_cells, current_cost, grid, min(maxcost, right_maxcost))
    else:
        up_visited_cells, up_maxcost = ([], float("inf"))

    if position[1]+1 <= len(grid)-1:
        down_visited_cells, down_maxcost = nextstep(costs,[position[0],position[1]+1],down_visited_cells,current_cost,grid,min(maxcost,right_maxcost,up_maxcost))
    else:
        down_visited_cells, down_maxcost = ([], float("inf"))

    if position[0]-1 >= 0:
        left_visited_cells, left_maxcost = nextstep(costs,[position[0]-1,position[1]],left_visited_cells,current_cost,grid,min(maxcost,right_maxcost,up_maxcost,down_maxcost))
    else:
        left_visited_cells, left_maxcost = ([], float("inf"))

    # Out of all four possible continuation paths, choose the one that has the least cost
    if min(right_maxcost,left_maxcost,up_maxcost,down_maxcost) == right_maxcost:
        return (right_visited_cells, right_maxcost)
    elif min(right_maxcost,left_maxcost,up_maxcost,down_maxcost) == up_maxcost:
        return (up_visited_cells, up_maxcost)
    elif min(right_maxcost,left_maxcost,up_maxcost,down_maxcost) == down_maxcost:
        return (down_visited_cells, down_maxcost)
    else:
        return (left_visited_cells, left_maxcost)

def drawpath(path,grid,outputtxt):
    drawn_path = grid.copy()
    for cell in path: # Changes all cells that are in the path to "x"
        drawn_path[cell[1]][cell[0]] = "X"
    for row in drawn_path: # Prints the new grid with path row by row
        rowlist = ""
        for cell in row:
            rowlist = rowlist + str(cell) +" "
        outputtxt.write("\n"+rowlist)



main()