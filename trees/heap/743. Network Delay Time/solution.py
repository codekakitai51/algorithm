class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for src, tar, wei in times:
            adj[src].append((tar, wei))
    
        minHeap = [(0, k)]
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
         
            for n2, w2 in adj[n1]:
                if not n2 in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return max(shortest.values()) if len(shortest) == n else -1
    
# Time: O(E * VlogV) = O(E * logV)