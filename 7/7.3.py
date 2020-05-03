x = map(int,input().split())
y = set()
for i in x:
    if i in x:
        print('yes')
    else:
        print('no')
        y.add(i)
