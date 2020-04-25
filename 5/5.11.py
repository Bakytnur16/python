n = int(input())
a = map(int, (input().split()))
x = int(input())
print(min(a, key=lambda a: abs(a - x)))
