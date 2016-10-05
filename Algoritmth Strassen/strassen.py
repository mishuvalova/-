import numpy as np


def read_matrix(n, m):
    c = []
    for _ in range(n):
        c.append([int(x) for x in input().split()])
    m[:n, :n] = np.matrix(c)
    return m


def split_matrix(m):
    l, r = np.hsplit(m, 2)
    m11, m21 = np.vsplit(l, 2)
    m12, m22 = np.vsplit(r, 2)
    return m11, m12, m21, m22


def strassen(a, b):
    if np.size(a) == 1:
        return np.dot(a, b)
    else:
        a11, a12, a21, a22 = split_matrix(a)
        b11, b12, b21, b22 = split_matrix(b)
        p1 = strassen(a11 + a22, b11 + b22)
        p2 = strassen(a21 + a22, b11)
        p3 = strassen(a11, b12 - b22)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a12, b22)
        p6 = strassen(a21 - a11, b11 + b12)
        p7 = strassen(a12 - a22, b21 + b22)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        return np.vstack((np.hstack((c11, c12)),
                          np.hstack((c21, c22))))


def print_matrix(m):
    for row in m:
        print(" ".join(map(str, row)))


def main():
    n = int(input())
    n_widening = 1
    while n_widening < n:
        n_widening *= 2
    a = np.zeros((n_widening, n_widening), dtype=int)
    b = np.zeros((n_widening, n_widening), dtype=int)
    result = strassen(read_matrix(n, a), read_matrix(n, b))
    print_matrix(result[:n, :n])


if __name__ == '__main__':
    main()
