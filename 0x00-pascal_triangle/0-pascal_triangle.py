#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n: Integer representing the number of rows in Pascal's Triangle.

    Returns:
    - List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

# Example usage
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

