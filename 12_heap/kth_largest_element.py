class Solution:
    def kth_largest_element(self, nums: list[int], k:int):
        # min heap data structure
        import heapq
        pq = []

        # add the first k element
        for i in range(k):
            heapq.heappush(pq, nums[i]) 


        for i in range(k, len(nums)):
            # check if a new larger number is found
            if nums[i] > pq[0]:
                heapq.heappop(pq) # remove the smallest element

                # add the current element to heap
                heapq.heappush(pq, nums[i])

        return pq[0]

                