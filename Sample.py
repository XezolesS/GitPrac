# 백준 12759번 문제
# 틱택토 정답 코드

board = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]

def is_win():
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
        
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return 0

num = int(input())

cnt = 0
res = 0
while res == 0 and cnt < 9:
    r, c = map(int, input().split())

    r -= 1
    c -= 1

    board[r][c] = num

    if num == 1:
        num = 2
    else:
        num = 1

    cnt += 1
    res = is_win()

print(res)