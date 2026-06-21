nums = [1, 2, 1, 1, 3, 2, 2]

class Solution:
    def majority_element(self, nums: list[int]):
        n = len(nums)

        count_el : dict = {}
        result = []
        mini = n // 3 + 1
        for num in nums:
            if num not in count_el.keys():
                count_el[num] = 1
            else:
                count_el[num]+=1

            if count_el[num] == mini:
                result.append(num)
            
            if len(result) == 2:
                break
        
        return result
    

sol = Solution()

result = sol.majority_element(nums)
print(result)