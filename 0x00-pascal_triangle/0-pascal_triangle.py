#!/usr/bin/python3
"""Pascal triangle script"""


def pascal_triangle(n: int):
    """Generate a pascal triangle with n rows.

    Args:
        n (int): Number of rows in the triangle

    Returns:
        list: List of lists containing each row to nth row
        or empty list if n <= 0.
    """
    triangle = [[1]]
    m = 2

    try:
        if n <= 0:
            return []

        if n == 1:
            return triangle

        for i in range(1, n):
            current_row = []
            previous_row = triangle[i - 1]
            for j in range(m):
                if j - 1 < 0:
                    previous_element_above = 0
                else:
                    previous_element_above = previous_row[j - 1]

                try:
                    next_element_above = previous_row[j]
                except IndexError:
                    next_element_above = 0

                current_new_element = previous_element_above + \
                    next_element_above
                current_row.append(current_new_element)
            triangle.append(current_row)
            m += 1

        return triangle
    except TypeError:
        pass
