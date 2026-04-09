class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        queue which the that came in
        add first than check if the top number is valid

        [(1, 0)]
        [(2, 1)]
        [(2, 1), (1, 2)] --> 3
        [(4, 4)]

        [1 2 1] 0 4 2 6

        1 [2 1 0] 4 2 6

        1 2 [1 0 4] 2 6

        ..
        """

        dq = deque([])
        res = []

        for i, num in enumerate(nums):
            while dq and num > dq[-1][0]:
                dq.pop()

            dq.append((num, i))

            if i >= k - 1:
                while dq and dq[0][-1] <= i - k:
                    dq.popleft()


                res.append(dq[0][0])



        return res




            
            