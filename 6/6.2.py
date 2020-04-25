n = int(input())
b = list(map(int, input().split()))
b.sort()
print(' '.join(map(str, b)))
