class Solution:
    def next_greater_element(self, nums1: list[int], nums2:list[int]):
        next_greater_element = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater_element[smaller_num] = num

            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_greater_element.get(num, -1))

        return ans