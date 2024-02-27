class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = sandwiches[::-1]
        while queue:          
            if not stack[-1] in queue:
                return len(queue)
         
            curStu = queue.popleft()
            
            if curStu == stack[-1]:
                stack.pop()
            else:
                queue.append(curStu)
            
        return len(queue)