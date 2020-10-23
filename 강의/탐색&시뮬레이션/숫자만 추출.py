import sys
sys.stdin = open("import.txt" , "rt")

str = input()
answerString = ""
res = 0
count = 0
for val in str:
    try:
        res = 10*res + int(val)
    except:   # 예외 처리 
        print(end='')

    # if val.isdigit():
    #     answerString += val

# answer = int(answerString)
for i in range(1, res+1):
    if res % i == 0:
        count += 1

print(res)
print(count)
