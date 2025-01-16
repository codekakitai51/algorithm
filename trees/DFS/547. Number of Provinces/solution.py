class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        L = len(isConnected)
        visited = [False] * L
        count = 0

        def helperDFS(city):
            for nei in range(L):
                if isConnected[city][nei] and not visited[nei]:
                    visited[nei] = True
                    helperDFS(nei)

        for city in range(L):
            if not visited[city]:
                visited[city] = True
                helperDFS(city)
                count += 1
        
        return count
            