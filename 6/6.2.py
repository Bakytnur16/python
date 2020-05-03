n = int(input())
a = list(map(int, input().split()))
a.sort()
print(*[x for x in a if x < 10])
