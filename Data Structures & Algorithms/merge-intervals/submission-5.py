class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_data = sorted(intervals, key=lambda x: x[0])
        ptr = 0
        res = [sorted_data[ptr]]

        for idx in range(1, len(sorted_data)):
            arr = sorted_data[idx]

            if arr[0] <= res[ptr][1] and arr[1] >= res[ptr][0]:
                res[ptr] = [
                            min(arr[0], res[ptr][0]),
                            max(arr[1], res[ptr][1])
                ]
            else:
                res.append(arr)
                ptr+= 1


        return res

            