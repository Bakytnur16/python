x = int(input())
i = 1
n = i
while i <= x:
    print(n, end=' ')
    i = i + 1
    n = i ** 2
    if n > x:
        break
