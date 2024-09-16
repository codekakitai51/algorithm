class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        for part in path.split('/'):
            if part == "..":
                if pathStack:
                    pathStack.pop()
            
            elif part == '.' or not part:
                continue
            
            else:
                pathStack.append(part)

        return '/' + '/'.join(pathStack)