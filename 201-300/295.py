class MedianFinder:

    def __init__(self):
        self.heap1, self.heap2 = [], []
        heapq.heapify(self.heap1)
        heapq.heapify(self.heap2)

    def addNum(self, num: int) -> None:
        if len(self.heap1) == len(self.heap2):
            if self.heap2 and num < self.heap2[0]:
                heapq.heappush(self.heap1, -num)
            elif self.heap2:
                val = heapq.heappop(self.heap2)
                heapq.heappush(self.heap1, -val)
                heapq.heappush(self.heap2, num)
            else:
                heapq.heappush(self.heap1, -num)
        else:
            if -num < self.heap1[0]:
                heapq.heappush(self.heap2, num)
            else:
                val = -heapq.heappop(self.heap1)
                heapq.heappush(self.heap2, val)
                heapq.heappush(self.heap1, -num)

    def findMedian(self) -> float:
        if (len(self.heap1) + len(self.heap2)) % 2 == 0:
            return (-self.heap1[0] + self.heap2[0]) / 2.0
        else:
            return -self.heap1[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()