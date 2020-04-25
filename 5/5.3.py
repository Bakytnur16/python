n = int(input())
print('+___ ' * int(n))
for i in range(n):
    print('|',(i+1),' / ', sep='', end='')
print()
print('|__\ '*int(n))
print('|    '*int(n))
