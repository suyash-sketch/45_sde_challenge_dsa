class Solution:
    def __init__(self):
        self.heap = []

    def initializeHeap(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def changeKey(self, index, new_val):
        if index < 0 or index >= len(self.heap):
            return

        old_val = self.heap[index]
        self.heap[index] = old_val

        if new_val > old_val:
            self._heapify_up(index)
        elif new_val < old_val:
            self._heapify_down(index)


    def extractMax(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return max_val

    def getMax(self):
        if len(self.heap) == 0:
            return None

        return self.heap[0]

    def heapSize(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2


    def _heapify_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
