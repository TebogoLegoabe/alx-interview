#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in range(n):
        matrix[row].reverse()
