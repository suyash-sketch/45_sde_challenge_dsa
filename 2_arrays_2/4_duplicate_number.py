nums = [4,1,3,2,2]

class Solution:
    # def find_duplicate(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     nums = sorted(nums)
    #     print(nums)
    #     duplicate_num = None
    #     for i in range(n - 1):
    #         if nums[i] == nums[i+1]:
    #             duplicate_num = nums[i]
    #             break
                
    #     return duplicate_num
    
    def find_duplicate(self, nums: list[int]) -> int:
        n = len(nums)

        # sum = 0
        sum_of_arr = sum(nums)

        if sum_of_arr % n != 0:
            duplicated_num = sum_of_arr % n
        else:
            duplicated_num = sum_of_arr // n

        return duplicated_num

ss = Solution()

answer = ss.find_duplicate(nums)
print(answer)