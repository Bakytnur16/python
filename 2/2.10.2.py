x = int(input())
y = int(input())
i = 1
while i < x:
    n = x + (x + x * 0.1) * i
    i += 1
    if n > y:
        break
print(int(n))
