import sys
sys.stdin = open('import.txt', 'rt')

# 행 검사
def checkSudoku(s):
    checkRow = [False for _ in range(10)]  # 행 검사
    checkCol = [False for _ in range(10)]  # 열 검사
    checkDia = [False for _ in range(10)]  # 대각선 검사

    for i in range(9):
        # 행, 열 검사
        for j in range(9):
            if checkRow[s[i][j]]:
                return False
            else:
                checkRow[s[i][j]] = True
            if checkCol[s[j][i]]:
                return False
            else:
                checkCol[s[j][i]] = True
        # 초기화
        checkRow = [False for _ in range(10)]  # 행 검사
        checkCol = [False for _ in range(10)]  # 열 검사

        if i == 0 or i == 3 or i == 6:
            for j in range(3):
                for k in range(3):
                    if checkDia[s[i+j][i+k]]:
                        return False
                    else:
                        checkDia[s[i+j][i+k]] = True
            checkDia = [False for _ in range(10)]

            for j in range(3):
                for k in range(3):
                    if checkDia[s[i+j][k]]:
                        return False
                    else:
                        checkDia[s[i+j][k]] = True
            checkDia = [False for _ in range(10)]
            for j in range(3):
                for k in range(3):
                    if checkDia[s[j][i+k]]:
                        return False
                    else:
                        checkDia[s[j][i+k]] = True
            checkDia = [False for _ in range(10)]

    return True


n = int(sys.stdin.readline())
for count in range(n):
    s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    if checkSudoku(s):
        print('Case %d: CORRECT' % (count + 1))
    else:
        print('Case %d: INCORRECT' % (count + 1))
    sys.stdin.readline()
