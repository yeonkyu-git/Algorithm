a, b = map(int, input().split())

def gcm_method (a,b):
    gcm = 1
    for k in range(2, min(a,b) + 1):
        while a % k == 0 and b % k == 0:
            a = a // k
            b = b // k
            gcm = gcm * k
            continue
    return gcm

print(gcm_method(a,b))
