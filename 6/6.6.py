def CountSort(list):
    sortList = [0] * 101
    for i in list:
        sortList[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortList[i], end='')
list = [int(i) for i in input().split()]
CountSort(list)
