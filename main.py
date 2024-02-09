from random import *

def main():
    print("What board size do you want?")

    while True:
        try:
            boardSize = int(input())
            break
        except:
            print("Print a number dumbass!")


    #TODO: Fix values to be all strings so it's prettier
    p1Board = [[0 for i in range(boardSize)]for j in range(boardSize)]
    p2Board = [[0 for i in range(boardSize)]for j in range(boardSize)]

    #TODO: Place ships
    placeRandomShip(p1Board)
    placeRandomShip(p2Board)

    print("Welcome to Battleships")

    while not isGameOver(p1Board) and not isGameOver(p2Board):
        print("Player 1's Turn:")
        printHiddenBoard(p2Board)
        print("Player 1: Where do you want to shoot? In format 'x,y'")

        while True:
            # try:
            action = input()
            coordinate_x, coordinate_y = action.split(",")
            print("You shot at ", coordinate_x, ", ", coordinate_y)
            coordinate_x,coordinate_y = int(coordinate_x)-1, int(coordinate_y)-1
            takeShot(p2Board, coordinate_x, coordinate_y)
            print("")
            break
            # # except:
            # #     print("Your action was not valid, try again")
        #TODO: Check if Player 1 won
        #Player 2's Turn:'
        print("Player 2's Turn:")

        printHiddenBoard(p1Board)
        print("Player 2: Where do you wanna shoot?")
        while True:
            # try:
            action = input()
            coordinate_x, coordinate_y = action.split(",")
            print("You shot at ",coordinate_x, ", ", coordinate_y)
            coordinate_x, coordinate_y = int(coordinate_x)-1, int(coordinate_y)-1
            takeShot(p1Board, coordinate_x, coordinate_y)
            break
            #  except:
            #     print("Your action was not valid, try again")
        #TODO: Check if Player 2 won

    printFinalBoard(p1Board, p2Board)
    if isGameOver(p1Board):
        print("Player 2 WON!")
    else:
        print("Player 1 WON!")


def takeShot(board, x, y):
    if board[x][y] == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "@"


def isGameOver(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                return False
    return True

def printFinalBoard(doubleArray1, doubleArray2):
    print("Player 1\t\t\t\t\t\t Player 2 ")
    for i in range(len(doubleArray1)):
        print(doubleArray1[i], "\t", doubleArray2[i])

def printHiddenBoard(board):
    for i in range(len(board)):
        print_line = []
        for j in range(len(board[i])):
            if board[i][j] == 1:
                print_line += [0]
            else:
                print_line += [board[i][j]]
        print(print_line)


def placeRandomShip(board):
    for i in range(4):
        shipPlacement = [randint(0,len(board)-1), randint(0,len(board)-1)]
        # print(shipPlacement)

        board[shipPlacement[0]][shipPlacement[1]] = 1


main()
