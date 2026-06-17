class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula = max(min(height_x, height_y)*(y-x))
        # 2 pointer approach

        i,j = 0,len(heights)-1
        result = 0
        while (i<j):
            area = min(heights[i], heights[j])*(j-i)
            result = max(result,area)
            if (heights[i] < heights[j]):
                i+=1
            else:
                j-=1

        return result