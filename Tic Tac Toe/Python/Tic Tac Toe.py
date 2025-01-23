
from random import randrange

board = [[0 for j in range(3)] for i in range(3)]
for a in range(3):
    for b in range(3):
        board[a][b] = (b+1)+a*3


#Represntation
def draw():
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

draw()

#To play availability and assign
def play(move, v):
    if type(move) == int:
        index(move)
        if type(board[ind_1][ind_2]) == int:
            board[ind_1][ind_2] = v
            draw()
            return True
    else:
        return False

#To play for index
def index(inpu):
    global ind_1
    global ind_2
    for a in range(3):
        for b in range(3):
            if inpu == board[a][b]:
                ind_1 = a
                ind_2 = b
                return True
    return False

#Computer Move
def comp_Move(x = randrange(1, 9)):
    while index(x) != True:
        x = randrange(1, 9)
    play(x, "X")
    return True
        
#User Move
def user_Move():
    user_input = int(input("Your move: "))
    while index(user_input) != True:
        user_input = int(input("Try again: "))
    print(user_input)
    play(user_input, "O")
    return True
        
def won():
    global winner
    for q in range(3):
        if board[q][0] == board[q][1] == board[q][2] or \
           board[0][q] == board[1][q] == board[2][q]:
            winner = True
            return True
    if board[0][0] == board[1][1] == board[2][2] or \
         board[0][2] == board[1][1] == board[2][0]:
        winner = True
        return True
    count = 0
    for a in range(1, 9):
        if index(a):
            count+=1
    if count > 0:
        return False
    else:
        move = ""
        winner = False
        return True

def gameplay():
    comp_Move(5)
    move =  True
    while won() != True:
        if move ==  True:
            user_Move()
            move = False
        else:
            comp_Move()
            move = True
    if winner == True:
        if move == True:
            print("Computer Won (X)!")
        else:
            move == False
            print("You Won (O)!")
    else:
        print("Ran out of moves!")

gameplay()








