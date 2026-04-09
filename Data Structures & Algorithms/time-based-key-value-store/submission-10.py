class TimeMap:

    def __init__(self):
        self.map_ = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map_[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map_[key]
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid][-1] <= timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1



        return res
                
