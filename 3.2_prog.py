def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    # Initialize an empty matrix for the result
    result_matrix = []

    # Perform element-wise addition
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)

    return result_matrix

# Example matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Add matrices
result = add_matrices(matrix_A, matrix_B)

# Print the result
if result:
    print("Matrix A:")
    for row in matrix_A:
        print(row)

    print("\nMatrix B:")
    for row in matrix_B:
        print(row)

    print("\nResultant Matrix (A + B):")
    for row in result:
        print(row)
