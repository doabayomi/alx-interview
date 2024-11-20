#!/usr/bin/python3
"""Clockwise Matrix Rotation
"""
from typing import List, Any


def rotate_2d_matrix(matrix: List[List[Any]]) -> None:
    """Rotates a n x n 2D matrix clockwise

    Args:
        matrix: The matrix being rotated
    """
    n = len(matrix[0])
    rotated_matrix = []
    for j in range(0, n):
        row = []
        for i in range(n-1, -1, -1):
            row.append(matrix[i][j])
        rotated_matrix.append(row)

    matrix.clear()
    matrix.extend(rotated_matrix)
