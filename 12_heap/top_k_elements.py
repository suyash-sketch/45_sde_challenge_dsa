import heapq

class Solution:
    def top_k_element(self, nums: list[int], k:int):
        heap = []
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

string = "aAAfffgggg"
string.lower()