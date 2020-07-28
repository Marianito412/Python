from colorama import Fore, Style

def createMaze():
    maze=[]
    maze.append(["X","#","="])
    maze.append(["=","=","="])
    maze.append(["=","#","="])
    maze.append(["=","=","="])
    maze.append(["#","#","="])
    maze.append(["Y","=","="])
    return maze

def validMove(maze, Moves):
    for k, pos in enumerate(maze[0]):
        if pos == "X":
            start = k
    i = start
    j = 0

    i = i + (Moves.count("R") - Moves.count("L"))
    j = j + (Moves.count("D") - Moves.count("U"))

    if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
        return False
    elif maze[j][i] == "#":
        return False

    return True

def printMaze(maze, moves):
    for k, pos in enumerate(maze[0]):
        if pos == "X":
            start = k
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i-=1
        if move == "D":
            j+=1
        if move == "U":
            j-=1
        if move == "R":
            i+=1
        maze[j][i] = f"{Fore.RED}={Style.RESET_ALL}"
    
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in maze]))
    


def findEnd(maze, Moves):
    for k, pos in enumerate(maze[0]):
        if pos == "X":
            start = k
    i = start
    j = 0
          
    i = i + (Moves.count("R") - Moves.count("L"))
    j = j + (Moves.count("D") - Moves.count("U"))

    if maze[j][i] == "Y":
        print("Found: ", Moves)
        return True

    return False

if __name__ == "__main__":
    maze = createMaze()
    q = [""]
    x = ""
    while not findEnd(maze, x):
        x = q.pop(0)
        for i in ["L","D","U","R"]:
            put = x+i
            if validMove(maze, put):
                q.append(put)
    
    printMaze(maze, x)
