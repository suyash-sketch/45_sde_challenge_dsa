class Solution:
    def backtrack(self, nums: list[int], used: list[bool], current: list[int], result: list[list[int]]):

        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            #skip already used elements
            if used[i]:
                continue

            used[i] = True
            current.append(nums[i])

            self.backtrack(nums, used, current, result)
            

            current.pop()
            used[i] = False

    def permutation(self, nums: list[int]):
       result = []
       used = [False] * len(nums)
       self.backtrack(nums, used,[], result)
       return result
   


sol = Solution()
nums = [1,2,3]
answer = sol.permutation(nums)
print(answer)


