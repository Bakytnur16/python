from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        string = ""
        amount = 0
        for matrix in self.matrix:
            if amount != 0:
                string += "\n"
            new_str = "\t".join(str(elem) for elem in matrix)
            string += new_str
            amount += 1
        return string

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))
        return result

    def __add__(self, other):
        result = Matrix
        result.matrix = []
        if self.size() == other.size():
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[0])):
                    x = self.matrix[i][j] + other.matrix[i][j]
                    temp.append(x)
                result.matrix.append(temp)
        else:
            raise MatrixError(self, other)
        return Matrix(result.matrix)

    def __mul__(self, alpha):
        if isinstance(alpha, int) or isinstance(alpha, float):
            result = []
            numbers = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = self.matrix[i][j] * alpha
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def transpose(self):
        t_matrix = list(zip(*self.matrix))
        self.matrix = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.matrix))
        return Matrix(t_matrix)

    __rmul__ = __mul__


exec(stdin.read())
