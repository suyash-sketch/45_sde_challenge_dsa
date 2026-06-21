class Solution:
    def find_sum(self, index, current_sum, arr: list[int], sums: list[int]):
        if index == len(arr):
            sums.append(current_sum)
            return
        
        # include current element 
        self.find_sum(index + 1, current_sum + arr[index], arr, sums)
        
        # exclude current element
        self.find_sum(index + 1, current_sum, arr, sums)

    def subset_sum(self, arr):
        sums = []
        self.find_sum(0,0,arr, sums)
        sums.sort()
        
        return sums
