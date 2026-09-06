class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """
        arr : mountain arry
            arr.length >= 3

            thier exist some index i with 0 < i < arr.length - 1
                arr[0] < arr[i] < arr[i - 1] < arr[i]
                arr[i] > arr[i + 1] > .. > arr[arr.length - 1]

            return the min index such that
                mountainArr.get(index) == target
                if such an index does not exist return - 1

                mid = min index such that mountainArr.get(index) == target

                
        """
        def lbinarySearch(l, r):
            best = -1
            while l <= r:
                mid = l + (r - l) // 2
                curr = mountainArr.get(mid)
                if curr == target:
                    return mid
                elif curr > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return best

        def rbinarySerach(l, r):
            best = -1
            while l <= r:
                mid = l + (r - l) // 2
                curr = mountainArr.get(mid)
                if curr == target:
                    return mid
                elif curr < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return best

        n = mountainArr.length()
        l, r = 1, n - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            left , right = mountainArr.get(mid - 1), mountainArr.get(mid + 1)
            curr = mountainArr.get(mid)

            if left < curr > right:

                leftSearch = lbinarySearch(0, mid)
                if leftSearch != -1:
                    return leftSearch
                rightSearch = rbinarySerach(mid+1, n - 1)
                if rightSearch != -1:
                    return rightSearch

                return -1
            elif curr < left:
                r = mid - 1
            elif curr < right:
                l = mid + 1

        return -1


