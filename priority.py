import heapq

from typing import TypeVar, Generic, Tuple


T = TypeVar("T")


class PriorityQueue(Generic[T]):
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

        self.count = 0

    def push(self, element: T, value: int) -> None:
        heapq.heappush(self.heap, (value, self.count, element))
        self.count += 1

    def pop(self) -> Tuple[T, int]:
        value = heapq.heappop(self.heap)

        return value[2], value[0]

    def __len__(self) -> int:
        return len(self.heap)

