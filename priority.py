import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

        self.count = 0

    def push(self, element, value):
        heapq.heappush(self.heap, (value, self.count, element))
        self.count += 1

    def pop(self):
        value = heapq.heappop(self.heap)

        return value[2], value[0]

    def __len__(self):
        return len(self.heap)

