class Solution(object):
    def trap(self, height):

        # APPROACH - 1 ( USING O(1) EXTRA SPACE )

        n = len(height)
        lmax, rmax, water = 0, 0, 0
        l, r = 0, n - 1 

        while l < r:
            if height[l] < height[r]:
                if lmax > height[l]:
                    water += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r]:
                    water += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1

        return water
 


        # APPROACH - 2 ( USING EXTRA SPACE )

        # n = len(height)
        # water = 0
        # left = [0] * n
        # left[0] = height[0]
        # right = [0] * n
        # right[n - 1] = height[n - 1]

        # for i in range(1, n):
        #     left[i] = max(left[i-1], height[i])
        # for i  in range(n-2, 0, -1):
        #     right[i] = max(right[i+1], height[i])

        # for i in range(1, n-1):
        #     if height[i] < left[i] and height[i] < right[i]:
        #         water += (min(left[i], right[i]) - height[i])
        # return water