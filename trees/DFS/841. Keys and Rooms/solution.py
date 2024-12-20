class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        keys = [0]

        while keys:
            roomNum = keys.pop()
            for key in rooms[roomNum]:
                if not seen[key]:
                    seen[key] = True
                    keys.append(key)
        
        return all(seen)