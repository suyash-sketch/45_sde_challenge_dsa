
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# #brute force approach 
# def rotate(matrix : list[list[int]]):
#     n = len(matrix)
#     rotated = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             rotated[j][n - i - 1] = matrix[i][j]

#     print(rotated)


# rotate(matrix)
# print(matrix)


def rotate(mat : list[list[int]]):
    n = len(mat)
    # first transpose the matrix
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    #reverse the transpose
    for i in range(n):
        mat[i].reverse()

    print(mat)

rotate(matrix)
# print(matrix)