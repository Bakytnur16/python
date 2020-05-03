from copy import deepcopy
 
 
class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])


    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        return Matrix(list(map(
                        lambda x, y: list(map(lambda z, w: z + w)),
                        self.matrix, other.matrix)))

    def __mul__(self, other):
        return Matrix([[i * other for i in list] for list in self.matrix])

    __rmul__ = __mul__


m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)
