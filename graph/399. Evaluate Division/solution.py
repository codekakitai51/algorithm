class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        # def bfs(src, target):
        #     if src not in adj or target not in adj:
        #         return -1
            
        #     q, visit = deque(), set()
        #     q.append([src, 1])
        #     visit.add(src)
        #     while q:
        #         n, w = q.popleft()
        #         if n == target:
        #             return w
        #         for nei, weight in adj[n]:
        #             if nei not in visit:
        #                 q.append([nei, w * weight])
        #                 visit.add(nei)
        #     return -1

        def dfs(src, target, visit, value):
            if src not in adj or target not in adj:
                return -1

            if src == target:
                return value

            visit.add(src)

            for n, w in adj[src]:
                if n not in visit:
                    res = dfs(n, target, visit, value * w)
                    if res != -1:
                        return res
            
            return -1

        # return [bfs(q[0], q[1]) for q in queries]
        return [dfs(q[0], q[1], set(), 1) for q in queries]