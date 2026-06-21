class Solution:
    def longestConsecutive(self, nums: list[int]):
        n = len(nums)

        if n == 0:
            return 0
        
        nums.sort()

        lastSmaller = float('-inf')
        count = 0
        longest = 1

        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                count+=1
                
                lastSmaller = nums[i]
            elif nums[i]!= lastSmaller:
                count=1
                lastSmaller = nums[i]
            
            longest = max(count, longest)
        
        return longest
    

nums = [100,4,200,1,2,3]

sol = Solution()
answer = sol.longestConsecutive(nums)
print(answer)