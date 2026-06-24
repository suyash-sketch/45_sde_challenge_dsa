class Solution:
    def kth_element(self, a:list[int], b:list[int], k):
        m = len(a)
        n = len(b)

        # ensure 'a' is the smaller arr
        if m > n:
           #swap a and b 
            return self.kth_element(b,a,k)

        # length of the left half
        left = k

        low = max(0, k - n)
        high = min(k,m)

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1

            # initialize l1, l2, r1, r2
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = a[mid1] if mid1 < m else float('inf')
            r2 = b[mid2] if mid2 < n else float('inf')


            # check if answer is found
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            elif l1> r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return -1