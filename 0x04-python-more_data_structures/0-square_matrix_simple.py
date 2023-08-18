#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for x in row:
            x_squared = x ** 2
            squared_row.append(x_squared)
        squared_matrix.append(squared_row)
    return squared_matrix
