n = input().split()
a = [int(i) for i in n]
max, index = a[0], 0
for i, x in enumerate(a):
    if x >= max:
        max = x
        index = i
print(max, index)
