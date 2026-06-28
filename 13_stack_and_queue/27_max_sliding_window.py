from collections import deque
from typing import List

class Solution:
    # Function to return the max of each sliding window of size k
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque to store indices of useful elements
        dq = deque()

        # Result list to store window maximums
        result = []

        # Loop through each element
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove all elements from the back that are smaller than current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index to deque
            dq.append(i)

            # Append max to result once the first window is completed
            if i >= k - 1:
                result.append(nums[dq[0]])

        # Return the result list
        return result

# Driver code
if __name__ == "__main__":
    obj = Solution()

    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    k = 3

    ans = obj.maxSlidingWindow(arr, k)

    # Print the result
    print(*ans)
