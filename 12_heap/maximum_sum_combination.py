import heapq

class Solution:
    def max_combination(self, nums1:list[int], nums2: list[int], k:int):
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        #initialize max heap with negative sums (since python has min heap)
        max_heap = [(-(nums1[0] + nums2[0]), 0, 0)] 

        # a set to keep track of visited index pairs
        visited = set()
        visited.add((0,0))

        result = []

        for _ in range(k):
            sum_neg, i, j = heapq.heappop(max_heap)

            result.append   (-sum_neg)

            #  Push next element from nums1 if not visited
            if i + 1 < len(nums1) and (i+1,j) not in visited:
                heapq.heappush(max_heap, ( -(nums1[i + 1] + nums2[j]),i+1, j))
                visited.add((i+1, j))

            # Push next element from nums2 if not visited  
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(nums1[i] + nums2[j+1]), i, j +1))
                visited.add((i,j+1))

        return result