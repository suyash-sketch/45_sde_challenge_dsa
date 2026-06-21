class Solution:
    def single_non_duplicate(self,arr:list[int]):
        n = len(arr)

        # if only one element
        if n == 1:
            return arr[0]

        # first element is unique one
        if arr[0] != arr[1]:
            return arr[0]

        #last element is unique one
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        low, high = 1, n - 2

        while low <= high:
            mid =   (low + high) // 2

            # check if middle element is unique one
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
               return arr[mid]
            # # If mid is in the left half (pairing is valid)
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
               low = mid + 1
            else:
               high = mid - 1
              
        return -1 


sol = Solution()
answer = sol.single_non_duplicate(arr=[1,1,2,3,3,4,4,5,5])
print(answer)            