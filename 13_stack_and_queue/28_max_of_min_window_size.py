class Solution:
    def maxOfMin(self, arr: list[int]) -> list[int]:
        n = len(arr)
        
        # Arrays to store indices of the next and previous smaller elements
        left = [-1] * n
        right = [n] * n
        
        # 1. Monotonic Stack to find the Previous Smaller Element (Left Boundary)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        # 2. Monotonic Stack to find the Next Smaller Element (Right Boundary)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        # Initialize the answer array. Size is (n + 1) so index matches window size exactly.
        # Fill with 0 (or -infinity if dealing with negatives, but problem usually implies positives)
        ans = [0] * (n + 1)
        
        # 3. For each element, find its max window size and update the answer array
        for i in range(n):
            # Calculate how far this element can stretch as the minimum
            window_size = right[i] - left[i] - 1
            ans[window_size] = max(ans[window_size], arr[i])
            
        # 4. Fill in the gaps by propagating the maximums backward
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
            
        # Return the slice from index 1 to n (since window sizes are 1 to n)
        return ans[1:]

# --- Example Traces ---
# sol = Solution()
# print(sol.maxOfMin([10, 20, 30, 50, 10, 70, 30])) 
# Output: [70, 30, 20, 10, 10, 10, 10]