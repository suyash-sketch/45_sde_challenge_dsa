matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def search_matrix(matrix: list[list[int]], target):
    m = len(matrix)
    n = len(matrix[0])

    # i = m - 1
    # j = n - 1

    # while i >= 0:
    #     while j >= 0:
    #         if matrix[i][j] == target:
    #             return True
    #         elif matrix[i][j] > target:
    #             i-=1
    #         elif matrix[i][j] < target:
    #             i+=1
            
    #         j-=1
    # return False

    low = 0
    high = n*m - 1

    while low <= high:
        mid = (low + high) // 2

        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False


answer = search_matrix(matrix, target)
print(answer)
