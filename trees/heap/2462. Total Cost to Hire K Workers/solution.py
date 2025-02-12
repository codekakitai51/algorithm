import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        L = len(costs)

        # 左側の候補をヒープ化
        heap1 = costs[:candidates]
        heapq.heapify(heap1)
        heap1Tail = candidates - 1

        # 右側の候補をヒープ化
        heap2Head = max(L - candidates, candidates)
        heap2 = costs[heap2Head:]
        heapq.heapify(heap2)

        res = 0
        for _ in range(k):
            if heap1 and (not heap2 or heap1[0] <= heap2[0]):  # heap1 の方が小さいか、heap2が空の場合
                res += heapq.heappop(heap1)
                if heap1Tail + 1 < heap2Head:
                    heap1Tail += 1
                    heapq.heappush(heap1, costs[heap1Tail])
            else:  # heap2 の方が小さい場合
                res += heapq.heappop(heap2)
                if heap1Tail < heap2Head - 1:
                    heap2Head -= 1
                    heapq.heappush(heap2, costs[heap2Head])

        return res
