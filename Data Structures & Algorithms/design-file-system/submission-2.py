class FileSystem:

    def __init__(self):
        self.p = {"/":-1, "":-1}
        

    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/" or path in self.p:
            return False

        split_path = path.split('/')
        parent = split_path[:-1]

        parent_path = "/".join(parent)
        if parent_path not in self.p:
            return False
            
        self.p[path] = value

        return True
        

    def get(self, path: str) -> int:
        return self.p[path] if path in self.p else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
