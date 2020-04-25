from sys import stdin
from copy import deepcopy


class Matrix():
    def __init__(self, a):
        self.a = deepcopy(a)

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in x]) for x in self.a])

    def size(self):
        return (len(self.a), len(self.a[0]))

m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)
