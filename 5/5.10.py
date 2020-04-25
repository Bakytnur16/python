n = input().split()
a = list(n)
ismin = 1000
for i in range(len(n)):
    s = int(a[i])
    if 0 < s < ismin:
        ismin = s
print(ismin)
