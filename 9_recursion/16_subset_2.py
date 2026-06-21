class Solution:
    def backtrack(self, start, nums: list[int], current: list[int], result: list[int]):
        result.append(list(current))

        for i in range(start, len(nums)):

            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])

            self.backtrack(i + 1, nums, current, result)

            current.pop()

    def subset_without_duplicate(self, nums: list[int]):
        nums.sort()
        result = []

        self.backtrack(0, nums, [], result)

        return result


sol = Solution()
nums = [1,2,2]

answer = sol.subset_without_duplicate(nums)

print(answer)
