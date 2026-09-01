class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        
        
        # total = 0

        # lakeStart = 0
        # displace = 0

        # left = 0
        # right = 0
        # for i, num in enumerate(height):
        #     if i == 0:
        #         continue
        #     if (num > height[i - 1]):
        #         if (left >= right): #
        #             left = num
        #             lakeStart = i
        #             continue
        #         elif (num < left): #check for lake

        #     if (num < height[lakeStart]):
        #         displace += num
        #         print("displace" + str(displace))
        #     else:
                
        #         print(lakeStart)
        #         print(i)
        #         water = height[lakeStart] * (i - lakeStart - 1) - displace
                
        #         print("water" + str(water))
        #         total += water
        #         lakeStart = i
        #         print("newStart" + str(lakeStart))
        #         displace = 0
        # return total


            # if (num < height[lakeStart]):
            #     if (lakeStart == 0): # marker
            #         lakeStart = i - 1
            #         #print(lakeStart)
            #     displace += num
            # else:
            #     water = min(num, height[lakeStart]) * (i - lakeStart - 2) - displace
            #     print("displace" + str(displace))
            #     print("range" + str((i - lakeStart - 2)))
            #     print(i)
            #     print(lakeStart)
            #     print("min" + str(min(num, height[lakeStart])))
            #     print("water" + str(water))
            #     total += water
            #     lakeStart = 0
            #     displace = 0

        return total
