prev = -1
x = 0
a = 0
e = int(input())
while e != 0:
    if prev == e:
        x += 1
    else:
        prev = e
        a = max(a, x)
        x = 1
    e = int(input())
a = max(a, x)
print(a)
