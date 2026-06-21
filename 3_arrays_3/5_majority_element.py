nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

class Solution:
    def majority_element(self, nums: list[int]):
        n = len(nums)
        count_el: dict = {}

        for num in nums:
            if num not in count_el.keys():
                count_el[num] = 1
            else:
                count_el[num] +=1

        # print(count_el)

        for num, count in count_el.items():
            if count > n / 2:
                return num

        return -1

    

ss = Solution()

answer = ss.majority_element(nums)
print(answer)

        