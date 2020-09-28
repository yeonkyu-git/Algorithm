a, b = map(int, input().split())

x = a if a > b else b
y = 0
index = 1

for i in range(1, b+1 if a > b else a+1):
    if a % i == 0 and b % i == 0:
        y = i

while True:
    try:
        if x % a == 0 and x % b == 0:
            break
        else:
            x += y
    except:
        print("error")

print(y)
print(x)


