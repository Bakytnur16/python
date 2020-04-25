a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
for i in sorted(list(a & b)):
    print(i, end=' ')
