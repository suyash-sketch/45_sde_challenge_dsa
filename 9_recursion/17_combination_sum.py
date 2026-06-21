class Solution:
    def find_combination(self, index, target, arr: list[int], ans:list[int], ds:list[int]):
        if index == len(arr):

            if target == 0:
                ans.append(list(ds))
            return

        if arr[index] <= target:
            ds.append(arr[index])
            self.find_combination(index, target - arr[index], arr, ans, ds)
            ds.pop()

        self.find_combination(index+1, target, arr, ans, ds)

    def combination_sum(self, candidates: list[int], target: int):
        ans = []
        ds = []
        self.find_combination(0, target,candidates,  ans, ds)
        return ans



arr = [2,3,4,7]
target = 7

sol = Solution()
result = sol.combination_sum(arr, target)
print(result)
