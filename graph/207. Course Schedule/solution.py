class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = { i:[] for i in range(numCourses) }
        for souce, dest in prerequisites:
            hashmap[souce].append(dest)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            if not hashmap[node]:
                return True
            
            visited.add(node)

            for nextNode in hashmap[node]:
                if not dfs(nextNode): return False
            visited.remove(node)
            hashmap[node] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False      
        return True