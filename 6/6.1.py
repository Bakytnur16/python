a = list(map(int, input().split()))
b = list(map(int, input().split()))
myList = sorted(a + b)
print(' '.join(map(str, myList)))
