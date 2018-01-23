board = [[],[],[],[],[]]
ks = 0
for i in range(5):
    for pos, char in enumerate(input()):
        if char == 'k':
            board[i].append(pos)
            ks += 1
if ks != 9:
    print('invalid')
    exit()
for idx, row in enumerate(board):
    if idx < 2:
        for n in row:
            if n+1 in board[idx+2] or n-1 in board[idx+2] or n+2 in board[idx+1] or n-2 in board[idx+1]:
                print('invalid')
                exit()
    if idx < 3:
        for n in row:
            if n + 2 in board[idx + 1] or n - 2 in board[idx + 1]:
                print('invalid')
                exit()
print('valid')




