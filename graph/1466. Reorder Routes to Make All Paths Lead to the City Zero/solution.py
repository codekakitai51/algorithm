class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in connections:
            adj[a].append((b, 1)) # original adj
            adj[b].append((a, 0)) # artificial adj
        
        def dfs(node, parent):
            nonlocal count

            for nei, sign in adj[node]:
                if nei != parent:
                    count += sign
                    dfs(nei, node)
            
            return count

        count = 0
        dfs(0, 0)

        return count
            