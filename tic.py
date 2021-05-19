import random

currentPositions = [x for x in range(1,10)] 

def printBoard():
    for x in range(10):
        if x == 0 or x == 9:
            print("\t    |     |")
        if x == 2:
            print(f"\t {currentPositions[0]}  |  {currentPositions[1]}  |  {currentPositions[2]}") 
        if x == 5:
            print("\t" + "-"*4 + "|" + "-"*5 + "|" + "-"*4)
            print(f"\t {currentPositions[3]}  |  {currentPositions[4]}  |  {currentPositions[5]}") 
            print("\t" + "-"*4 + "|" + "-"*5 + "|" + "-"*4)
        if x == 6:
            print(f"\t {currentPositions[6]}  |  {currentPositions[7]}  |  {currentPositions[8]}") 

def symbolSelect():
    symbolSelected = False 
    playerSymbol = ""

    while symbolSelected != True:
        playerSymbol = input("'X' or 'O'\n")
        if playerSymbol == 'X' or playerSymbol == 'O':
            symbolSelected = True
    if playerSymbol == "X":
        return ['X','O']
    else:
        return ['O','X']

def botMove(botSymbol):

    pass

def positionSelect(symbols):
    printBoard()
    playerSelection = input("\tPick a spot (1-9)\n")
    try:
        playerSelection = int(playerSelection)
        if currentPositions.index(playerSelection) in symbols:
            print("That spot is already taken, choose another")
            return positionSelect(symbols)

        if playerSelection <=0 or playerSelection >= 10:
           print(f"{playerSelection} is outside the range of the grid")
           return positionSelect(symbols)
        return currentPositions.index(playerSelection)
    
    except ValueError:
        print(f"{playerSelection} is not a valid spot")
        return positionSelect(symbols)

def winCheck(symbols):
    if int not in currentPositions:
        return 
    solutions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
    winner = ""
    for symbol in symbols:
        for solution in solutions:
            isWinner = all(currentPositions[position] == symbol for position in solution)
            if isWinner:
                print("WIN")
             
if __name__ == "__main__":
    play = True
    symbols = symbolSelect()
    userSymbol = symbols[0]
    botSymbol = symbols[1]
    while play:
        currentPositions[positionSelect(symbols)] = userSymbol
        winCheck(symbols)

