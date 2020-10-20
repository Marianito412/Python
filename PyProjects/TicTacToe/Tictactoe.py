winCombos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3]]

player = "X"
ai = "E"
playerMoves = []
aiMoves = []

def gameWon(playerMoves, aiMoves):
    for combo in winCombos:
        if set(combo).issubset(playerMoves):
            print("You have won!!")
            return True
        if set(combo).issubset(aiMoves):
            print("You have been beaten, what a worthless piece of shit")
            return True
    return False

def playerTurn(board):
    move = input("Your turn (xy): ")
    moves = list(move)
    x, y = moves
    board[int(y)-1][int(x)-1] = player
    playerMoves.append((3*(int(y)-1)) + (int(x)-1)+1)
    return board

def aiTurn(board):
    for row in range(len(board)):
        for item in range(len(board[row])):
            if board[row][item] != player and board[row][item] != ai:
                board[row][item] = ai
                aiMoves.append((3*row) + item+1)
                return board

def Game():
    board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
    while not gameWon(playerMoves, aiMoves):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
        board = playerTurn(board)
        board = aiTurn(board)
        print(playerMoves)
        print(aiMoves)
        
if __name__ == '__main__':
    Game()
