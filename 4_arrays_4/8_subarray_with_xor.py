nums = [4, 2, 2, 6, 4]
k = 6

class Solution:
    def subarraysWithXorK(self, nums, k):
        freq = {0:1}

        prefixXor = 0

        count = 0

        for num in nums:
            prefixXor ^= num

            target = prefixXor ^ k

            if target in freq:
                count +=freq[target]

            freq[prefixXor] = freq.get(prefixXor, 0) + 1
        
        return count

sol = Solution()
answer = sol.subarraysWithXorK(nums, k)
print(answer)