board = []
count = 1
for i in range(5):
    if i % 2 == 1:
        row = ["-" * 10]
        board.append(row)
        continue
    else:
        row = [f"{count} | {count+1} | {count+2}"]
        board.append(row)
        count += 3

for i in range(len(board)):
    for j in range(len(board[0])):
        print(f"{board[i][j]}")
        
# 1 = board[0][0]
# 2 = board[0][4]
# 3 = board[0][8]
# 4 = board[2][0]
# 5 = board[2][4]
# 6 = board[2][8]
# 7 = board[3][0]
# 8 = board[3][4]
# 9 = board[3][8]