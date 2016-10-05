import sys
import numpy as np
import numpy


def split_matrix(m):
    l, r = np.hsplit(m, 2)
    m11, m21 = np.vsplit(l, 2)
    m12, m22 = np.vsplit(r, 2)
    return m11, m12, m21, m22


def strassen(m1, m2):
    if np.size(m1) == 1:
        return np.dot(m1, m2)
    else:
        a11, a12, a21, a22 = split_matrix(m1)
        b11, b12, b21, b22 = split_matrix(m2)
        s1 = strassen(a11 + a22, b11 + b22)
        s2 = strassen(a21 + a22, b11)
        s3 = strassen(a11, b12 - b22)
        s4 = strassen(a22, b21 - b11)
        s5 = strassen(a11 + a12, b22)
        s6 = strassen(a21 - a11, b11 + b12)
        s7 = strassen(a12 - a22, b21 + b22)
        c11 = s1 + s4 - s5 + s7
        c12 = s3 + s5
        c21 = s2 + s4
        c22 = s1 - s2 + s3 + s6
        return np.vstack((np.hstack((c11, c12)),
                          np.hstack((c21, c22))))


def print_matrix(m):
    for row in m:
        print(" ".join(map(str, row)))


def main():
    n = int(input())
    n_round = 1
    while n_round < n:
        n_round *= 2
    m1 = np.zeros((n_round, n_round), dtype=int)
    m2 = np.zeros((n_round, n_round), dtype=int)
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    m1[:n, :n] = numpy.matrix(a)
    b = []
    for i in range(n):
        b.append([int(x) for x in input().split()])
    m2[:n, :n] = numpy.matrix(b)

    resm = strassen(m1, m2)
    print_matrix(resm[:n, :n])


if __name__ == '__main__':
    main()
