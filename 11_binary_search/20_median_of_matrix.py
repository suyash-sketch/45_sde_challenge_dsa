import bisect

class Solution:
    def count_less_equal(self,row, mid):
        return bisect.bisect_right(row, mid)

    
    def find_median(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        low = min( row[0] for row in matrix)
        high = max(row[0] for row in matrix)

        while low < high:
            mid = (low + high) // 2
            count = 0
         
            for row in matrix:
                count += self.count_less_equal(row, mid)

            if count < (rows * cols + 1) // 2:
                low = mid + 1
            else:
                high = mid - 1

        return low
             