array =  [10, 5, 2, 7, 1, 9]
k = 15
class Solution:
    def longest_subarray(self, nums:list[int], k):
        n = len(nums)

        mpp = {}
        maxi = 0
        
        curr_sum = 0

        for i in range(n):
            curr_sum+= nums[i]

            if curr_sum == k:
                maxi = i + 1

            rem = curr_sum - k
            if rem in mpp:
                length = i - mpp[rem]
                maxi = max(maxi, length)

            if curr_sum not in mpp:
                mpp[curr_sum] = i
        
        return maxi
    
sol = Solution()

answer = sol.longest_subarray(array, k)

print(answer)