nums = [-1,0,1,2,-1,-4]

class ListNode:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next

class Solution:
    def three_sum(self, nums:list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i],nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
    
                    while left < right and nums[right] == nums[right + 1]:
                        right-=1

                elif total < 0:
                    left +=1
                else:
                    right -=1

        return result
                
