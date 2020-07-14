def createMaze():
    maze=[]
    maze.append([" ","#","X"])
    maze.append([" "," "," "])
    maze.append(["#","#"," "])
    maze.append([" "," "," "])
    maze.append([" ","#","#"])
    maze.append([" "," ","Y"])
    return maze

def validMove(maze, Moves):
    for k, pos in enumerate(maze[0]):
        if pos == "X":
            start = k
    i = start
    j = 0
    #for move in Moves:
    #    if move == "L":
    #        i-=1
    #    if move == "D":
    #        j+=1
    #    if move == "U":
    #        j-=1
    #    if move == "R":
    #        i+=1
#
    #    if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
    #        return False
    #    elif maze[j][i] == "#":
    #        return False
    i = i + (Moves.count("R") - Moves.count("L"))
    j = j + (Moves.count("D") - Moves.count("U"))

    if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
        return False
    elif maze[j][i] == "#":
        return False
        
    return True

def findEnd(maze, Moves):
    for k, pos in enumerate(maze[0]):
        if pos == "X":
            start = k
    i = start
    j = 0
    #for move in Moves:
    #    if move == "L":
    #        i -=1
    #    if move == "D":
    #        j+=1
    #    if move == "U":
    #        j-=1
    #    if move == "R":
    #        i+=1
#
    #    if maze[j][i] == "Y":
    #        print("Found: ", Moves)
    #        return True
    #        
    i = i + (Moves.count("R") - Moves.count("L"))
    j = j + (Moves.count("D") - Moves.count("U"))

    if maze[j][i] == "Y":
        print("Found: ", Moves)
        return True

    return False

maze = createMaze()
q = [""]
x = ""
while not findEnd(maze, x):
    x = q.pop(0)
    for i in ["L","D","U","R"]:
        put = x+i
        if validMove(maze, put):
            q.append(put)
