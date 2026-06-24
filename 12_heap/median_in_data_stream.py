import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num:int):
        heapq.heappush(self.max_heap, -num)

        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, - heapq.heappop(self.min_heap))

    def fin_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        return - self.max_heap[0]
        