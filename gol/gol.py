alive = [(0, 0), (0, -1),(-1, 0), (1, 0), (-1, 1)]
newborns = []
still_alive = []
current_position = (0, 0)
generation = 0

def display():
    print(20 * '\n')
    print('Generation:', generation, 'Population:', len(alive))
    current_row = current_position[0] - 9
    current_column = current_position[1] - 9
    while current_row < current_position[0] + 10:
        pstring = ''
        while current_column < current_position[1] + 10:
            if (current_row, current_column) in alive:
                pstring = pstring + '#'
                current_column = current_column + 1
            else:
                pstring = pstring + '-'
                current_column = current_column + 1
        print(pstring)
        current_row = current_row + 1
        current_column = current_position[1] - 9
    print('done')

def countn(cell):
    northwest = (cell[0] - 1, cell[1] - 1)
    north = (cell[0] - 1, cell[1])
    northeast = (cell[0] - 1, cell[1] + 1)
    east = (cell[0], cell[1] + 1)
    southeast = (cell[0] + 1, cell[1] + 1)
    south = (cell[0] + 1, cell[1])
    southwest = (cell[0] + 1, cell[1] - 1)
    west = (cell[0], cell[1] - 1)
    neighbors = [northwest, north, northeast, east, southeast, south, southwest, west]
    liveneighbors = 0
    for n in neighbors:
        if n in alive:
            liveneighbors = liveneighbors + 1
    return(liveneighbors)

def countsurvivors():
    global alive
    global still_alive
    for cell in alive:
        if countn(cell) == 2 or countn(cell) == 3:
            still_alive.append(cell)

def countnewborns():
    global newborns
    global alive
    for cell in alive:
        northwest = (cell[0] - 1, cell[1] - 1)
        north = (cell[0] - 1, cell[1])
        northeast = (cell[0] - 1, cell[1] + 1)
        east = (cell[0], cell[1] + 1)
        southeast = (cell[0] + 1, cell[1] + 1)
        south = (cell[0] + 1, cell[1])
        southwest = (cell[0] + 1, cell[1] - 1)
        west = (cell[0], cell[1] - 1)
        neighbors = [northwest, north, northeast, east, southeast, south, southwest, west]
        for n in neighbors:
            if n not in alive:
                if countn(n) == 3:
                    if n not in newborns:
                        newborns.append(n)

def nextgen():
    global still_alive
    global newborns
    global generation
    global alive
    countnewborns()
    countsurvivors()
    alive = []
    for survivor in still_alive:
        alive.append(survivor)
    for newborn in newborns:
        alive.append(newborn)
    still_alive = []
    newborns = []
    generation = generation + 1

def main(command):
    global current_position
    while command != 'quit':
        display()
        command = input("Enter a command: ")
        if command == 'w':
            current_position = (current_position[0] - 1, current_position[1])
            display()
        elif command == 'a':
            current_position = (current_position[0], current_position[1] - 1)
            display()
        elif command == 's':
            current_position = (current_position[0] + 1, current_position[1])
            display()
        elif command == 'd':
            current_position = (current_position[0], current_position[1] + 1)
            display
        elif command == '':
            nextgen()

main('work dammit')
