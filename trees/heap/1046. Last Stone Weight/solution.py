class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # because python doesn't have max heap, we need to use -s to make it a min heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            
        if len(stones) == 0: return 0 # if all stones are smashed
        return abs(stones[0])