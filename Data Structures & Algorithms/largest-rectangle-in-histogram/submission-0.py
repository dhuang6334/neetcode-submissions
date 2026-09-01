class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
        
        # stack = []
        # indices = []
        # area = 0
        # for i in range(len(heights) + 1):
        #         if (i != len(heights)):
        #             height = heights[i]
        #     # if (i > 0 and stack[-1] >= height):
        #         lastInd = i
        #         while(len(stack) > 0 and (i == len(heights) or stack[-1] >= height)):
        #             print(stack)
        #             print(indices)
        #             stack.pop()
        #             lastInd = indices.pop()
                    
        #             print(max(height, height*(i-lastInd + 1)))
        #             print(area)
        #             if (max(height, height*(i-lastInd + 1)) > area):
        #                 area = max(height, height*(i-lastInd + 1))
        #                 print(area)
        #                 print("special")
        #         stack.append(height)
        #         indices.append(lastInd)
            # else:
            #     stack.append(height)
            #     indices.append(i)
            #     if (height > area):
            #         area = height
            #         print(area)

        # while (len(stack) > 0):
        #     if (len(stack) > 1):
        #         calc = stack.pop()*(indices.pop() - indices[-1] + 1)
        #         if (calc > area):
        #             area = calc
        #     elif (stack[-1] > area):
        #         area = stack.pop()
        #         indices.pop()
        #     else:
        #         stack.pop()
        #         indices.pop()

        return area