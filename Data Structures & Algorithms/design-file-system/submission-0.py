class FileSystem:
    def __init__(self):
        self.paths = {'':-1}

    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/":
            return False
        paths = path.split("/")

        parent, curr = paths[:-1], paths[-1]
        parent_path = "/".join(parent)
        print(self.paths, parent_path)
        if parent_path in self.paths and path not in self.paths:
            self.paths[path] = value
        else:
            return False

        return True

    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
