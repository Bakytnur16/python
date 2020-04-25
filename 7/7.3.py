x = [int(s) for s in input().split()]
y = set()
for num in x:
    if num in y:
        print('YES')
    else:
        print('NO')
        y.add(num)
