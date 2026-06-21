class Solution:
    def nth_root(self, n:int,m:int):
        low, high = 1,m

        while low <= high:
            mid = (low + high) // 2

            ans = 1
            for _ in range(n):
                ans = ans*mid
                if ans > m:
                    break

            if ans == m:
                return mid

            if ans < m:
                low = mid +1
            else:
                high = mid - 1

        return -1