class Solution:
    def trap(self, height: List[int]) -> int:
        
        waterLevel = 0
        l = 0
        r = len(height) - 1
        trapped = 0
        while l <= r:
            waterLevel = max(waterLevel, min(height[l], height[r]))
            # print(waterLevel)

            if l == r:
                if height[l] < waterLevel:
                    trapped += waterLevel - height[l]
                break
            
            
            if height[l] < height[r]:
                if height[l] < waterLevel:
                    trapped += waterLevel - height[l]
                l += 1
            elif height[l] > height[r]:
                if (height[r] < waterLevel):
                    trapped += waterLevel - height[r]

                r -= 1
            else:
                if height[l] < waterLevel:
                    trapped += waterLevel - height[l]
                l += 1

                if (height[r] < waterLevel):
                    trapped += waterLevel - height[r]

                r -= 1

            print(trapped)
        return trapped
