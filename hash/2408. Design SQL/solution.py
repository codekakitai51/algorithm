class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}  # Stores table data
        self.nextId = {}  # Stores the next available row ID for each table
        self.columns = {}  # Stores column count for each table
        
        for i in range(len(names)):
            self.tables[names[i]] = []  # Table starts empty
            self.nextId[names[i]] = 1  # First row ID starts at 1
            self.columns[names[i]] = columns[i]  # Store column counts

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables or len(row) != self.columns[name]:
            return False
        
        self.tables[name].append([str(self.nextId[name])] + row)
        self.nextId[name] += 1
        return True
    
    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return
        
        self.tables[name] = [row for row in self.tables[name] if int(row[0]) != rowId]
        

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        
        for row in self.tables[name]:
            if int(row[0]) == rowId:
                if 0 <= columnId < len(row):
                    return row[columnId]
                else:
                    return "<null>"
        
        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        
        return [",".join(row) for row in self.tables[name]]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)