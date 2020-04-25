a = int(input())
Max = a
n = 0
while a != 0:
    if a > Max:
        Max = a
        n = 1
    elif a == Max:
        n += 1
    a = int(input())
print(n)
