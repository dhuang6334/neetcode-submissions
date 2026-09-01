class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        size = len(heights)
        j = size - 1

        out = 0
        while (i < j):
            area = (j - i) * min(heights[i], heights[j])
            if (area > out):
                out = area
            
            if (heights[j] > heights[i]):
                i += 1
            elif (heights[j] < heights[i]):
                j -= 1
            else:
                i += 1
                j -= 1

        return out