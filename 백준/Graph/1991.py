n = int(input())
s= [[0] * 3 for i in range(n)]

def preorder(a):
    print(a, end="")
    if s[ord(a) - 65][1] != ".":
        preorder(s[ord(a) - 65][1])
    if s[ord(a) - 65][2] != ".":
        preorder(s[ord(a) - 65][2])

def inorder(a):
    if s[ord(a) - 65][1] != ".":
        inorder(s[ord(a) - 65][1])
    print(a, end='')
    if s[ord(a) - 65][2] != ".":
        inorder(s[ord(a) - 65][2])

def outorder(a):
    if s[ord(a) - 65][1] != ".":
        outorder(s[ord(a) - 65][1])
    if s[ord(a) - 65][2] != ".":
        outorder(s[ord(a) - 65][2])
    print(a, end='')

for i in range(n):
    a, b, c = map(str, input().split())
    a_ = ord(a) - 65
    s[a_][0], s[a_][1], s[a_][2] = a, b, c


preorder('A')
print()
inorder('A')
print()
outorder('A')