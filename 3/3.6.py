p = int(input()) * 0.01
a = int(input())
b = int(input())
now_cash = a + b + p * (a + b)
print(int(now_cash), round(100 * (now_cash - int(now_cash))))
