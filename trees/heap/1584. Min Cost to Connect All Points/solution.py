class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = {i: i for i in range(self.N)}
        self.rank = {i: 1 for i in range(self.N)}

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]    

        return p 

    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.par[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.par[root1] = root2
        else:
            self.par[root2] = root1
            self.rank[root1] += 1

        return True

class Solution:
# Kruskal's algorithm(using Union-Find) T: O(E * logV) S: O(E)
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        N = len(points)
        edgesMinHeap = []
        for n1 in range(N):
            x1, y1 = points[n1]
            for n2 in range(n1 + 1, N):
                x2, y2 = points[n2]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(edgesMinHeap, [dist, n1, n2])
        
        unionFind = UnionFind(N)
        edgesUsed = 0
        minCostPass = 0
        while edgesUsed < N - 1:
            dist, n1, n2 = heapq.heappop(edgesMinHeap)
            if unionFind.find(n1) == unionFind.find(n2):
                continue
            unionFind.union(n1, n2)
            edgesUsed += 1
            minCostPass += dist
        
        return minCostPass

# Prim's algorithm T: O(E * logV)
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #     N = len(points)
    #     adj = {i: [] for i in range(N)} # i: list of [cost, node]
    #     for i in range(N):
    #         x1, y1 = points[i]
    #         for j in range(i + 1, N):
    #             x2, y2 = points[j]
    #             dist = abs(x1 - x2) + abs(y1 - y2)
    #             adj[i].append([dist, j])
    #             adj[j].append([dist,i])

    #     # Prim's
    #     res = 0
    #     visit = set()
    #     minH = [[0, 0]] # [cost, point]
    #     while len(visit) < N:
    #         cost, i = heapq.heappop(minH)
    #         if i in visit:
    #             continue
    #         visit.add(i)
    #         res += cost

    #         for neiCost, nei in adj[i]:
    #             if nei not in visit:
    #                 heapq.heappush(minH, [neiCost, nei])
            
    #     return res
