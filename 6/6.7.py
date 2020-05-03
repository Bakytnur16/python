a = int(input())
man = sorted([input().split() for i in range(a)], key=lambda x:x[1], reverse=True)
for j in man:
    print(*j)
