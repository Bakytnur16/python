n = input().split()
a = [int(i) for i in n]
ismin = 0
ismax = 0
for i in range(1, len(a)):
    if a[i] > a[ismax]:
        ismax = i
    if a[i] < a[ismin]:
        ismin = i
a[ismin], a[ismax] = a[ismax], a[ismin]
print(' '.join([str(i) for i in a]))
