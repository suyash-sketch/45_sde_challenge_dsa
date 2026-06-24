class Solution:
    def count_students(self, arr: list[int], pages: int):
        n = len(arr)
        students = 1
        pages_student = 0

        for i in range(n):
            if pages_student + arr[i] <= pages:
                pages_student += arr[i]
            else:
                students+=1
                pages_student = arr[i]

        return students
        
        
    def find_pages(self, arr: list[int], m: int):
        n = len(arr)

        if m > n:
            return -1

        low = max(arr)
        high = sum(arr)

        for pages in range(low, high + 1):
            if self.count_students(arr,pages) == m:
                return pages

        return low