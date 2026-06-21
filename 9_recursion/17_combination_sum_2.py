from typing import List
class Solution:
    def find_combination(self, index, target, arr: List[int], ans: List[int], ds: List[int]):
        if target == 0:
            ans.append(list(ds))
            return
        
        for i in range(index, len(arr)):
            if i > index and arr[i] ==  arr[i - 1]:
                continue #skip duplicates to avoid repeated combinations
                
            if arr[i] > target:
                break

            ds.append(arr[i])

            self.find_combination(i+1, target - arr[i], arr, ans, ds)
            ds.pop()


    def combination_sum(self, candidate: List[int], target: int):
        candidate.sort()
        ans  = []
        ds = []
        self.find_combination(0,target, candidate,ans,ds)
        return ans

sol = Solution()
answer = sol.combination_sum([2,3,4,7],7)
print(answer)

