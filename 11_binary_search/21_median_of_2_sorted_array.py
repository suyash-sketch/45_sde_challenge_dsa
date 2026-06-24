class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            r1 = float('inf') if cut1 == m else nums1[cut1]
            
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r2 = float('inf') if cut2 == n else nums2[cut2]


            if l1 <= r2 and l2 <= r1:

                if (m + n) % 2 != 0:
                    return float(max(l1,l2))
                else:
                    return (max(l1,l2) + min(r1,r2)) / 2.0

            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0
                