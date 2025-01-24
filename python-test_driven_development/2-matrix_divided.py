#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor to divide all elements of the matrix by.
    
    Returns:
        list: A new matrix with all elements divided by div.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each element in each row of matrix is an integer or a float
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows in matrix have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is an integer or a float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero to avoid division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Return a new matrix with each element divided by div and rounded to 2 decimal places
    for row in matrix:
        return [[round(num / div, 2) for num in row]]
