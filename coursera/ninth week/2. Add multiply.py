from sys import stdin
from copy import deepcopy


class Matrix (object):
    def __init__(self, mat):
        self.mat = mat
        self.row = len(mat)
        self.col = len(mat[0])
        self._matRes = []
        self.__s = ''

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.mat)

    def __mul__(self, other):
        res = deepcopy(self.mat)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.row):
                for j in range(self.col):
                    res[i][j] *= other
            return Matrix(res)
        self._matRes = [[0 for r in range(other.col)] for c in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(other.row):
                    self._matRes[i][j] += self.mat[i][k] * other.mat[k][j]
        return Matrix(self._matRes)

    __rmul__ = __mul__

    def size(self):
        return (self.row, self.col)

    def __add__(self, other):
        self._matRes = [[0 for r in range(self.col)] for c in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self._matRes[i][j] += self.mat[i][j] + other.mat[i][j]
        return Matrix(self._matRes)


exec(stdin.read())
