n = input().split()
a = [int(i) for i in n]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=' ')
