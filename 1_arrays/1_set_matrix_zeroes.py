from configparser import RawConfigParser


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1,1,1],[1,0,1],[1,1,1]]

# def setZeroes(matrix: list[list[int]]):
#     m = len(matrix) #rows
#     n = len(matrix[0]) #cols
    
#     zero_list = []

#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == 0:
#                 zero_list.append([i,j])
    
#     for i, j in zero_list:
#         col = 0
#         row = 0
#         while col < n:
#             matrix[i][col] = 0
#             col+=1

#         while row < m:
#             matrix[row][j] = 0
#             row +=1
            
# setZeroes(matrix)
# print(matrix)


def setZeroes(matrix: list[list[int]]):
    m = len(matrix)     #row
    n = len(matrix[0])  #col
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for col in range(n):
                  if matrix[i][col] != 0:
                     matrix[i][col] = -1
                
                for row in range(m):
                    if matrix[row][j] != 0:
                        matrix[row][j] = -1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


setZeroes(matrix)
print(matrix)