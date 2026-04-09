class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left=0
        # right=len(height)-1
        # total=0
        # while left<right:
        #     total = max(total, min(height[left],height[right]) * abs(right-left))
        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return total
        l,r = 0,len(height)-1
        maxl,maxr = height[l],height[r]
        largest = max(height)
        ans = 0
        # print(ans)

        while (r-l)*largest>ans:
            if height[l]==maxl or height[r]==maxr:
                ans = max(ans,min(maxr,maxl)*(r-l))
            if maxl<=maxr:
                l += 1
                if height[l]>maxl:
                    maxl = height[l]
            else:
                r -= 1
                if height[r]>maxr:
                    maxr = height[r]
        
        return ans


        