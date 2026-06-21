nums = [1,0,-1,0,-2,2]
target = 0

class Solution:
    def four_sum(self,nums:list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i+1, n):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left],nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left+=1

                        while left < right  and nums[right] == nums[right - 1]:
                            right-=1

                        left+=1
                        right-=1
                    elif total < target:
                        left+=1
                    else:
                        right-=1

        return result
    

sol = Solution()
answer = sol.four_sum(nums, target)
print(answer)