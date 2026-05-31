class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        [1,2]
        [1,2]
        """
        
        one = m - 1
        two = n - 1
        three = len(nums1) - 1

        while one >= 0 and two >= 0:
            if nums1[one] < nums2[two]:
                nums1[three] = nums2[two]
                two -= 1
            else:
                nums1[three] = nums1[one]
                one -= 1

            three -= 1

        if two >= 0:
            for i in range(three, -1, -1):
                nums1[i] = nums2[two]
                two -= 1

        



