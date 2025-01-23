board = [[i*j for i in range(1, 17)] for j in range(1, 17)]

def dd(n):
    n = str(n)
    while len(n)<3:
        n = " "+n
        if len(n) < 3:
            n = n + " "
    return n

n = len(board)
print("+---------"*n, '+', sep="")
for a in range(n):
    print("|         "*n, '|', sep="")
    for b in range(n):
        print(f"|   {dd(board[a][b])}   ", end = "")
    print("|")
    print("|         "*n, '|', sep="")
    print("+---------"*n, '+', sep="")
    
