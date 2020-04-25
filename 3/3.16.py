s = input()
if len(s) > 1 and s.find('@') != -1:
    print(s.replace('@', ''), sep='')
elif s.find('@') == -1:
    print(s)
