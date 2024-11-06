class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        seen = {startGene}

        while q:
            node, step = q.popleft()
            if node == endGene:
                return step

            for i in range(len(node)):
                for c in "ACGT":
                    newNode = node[:i] + c + node[i + 1:]
                    if newNode not in seen and newNode in bank:
                        seen.add(newNode)
                        q.append((newNode, step + 1))
        
        return -1