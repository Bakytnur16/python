from copy import deepcopy


class Matrix():
    def __init__(self, a):
        self.a = deepcopy(a)

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in x]) for x in self.a])

    def size(self):
        return (len(self.a), len(self.a[0]))

m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))
