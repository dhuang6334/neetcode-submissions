class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            res += 1
        
        return res
        
        
        
        # jumps = [0] * len(nums)
        # res = 0
        # for i in range(len(nums)): # BFS on list
        #     if (jumps[i] >= res): # only explore when not visited aka not on a lower level
        #         res += 1
        #         for j in range(nums[i]):
        #             j += 1
        #             if (i + j < len(nums) and jumps[i+j] == 0):
        #                 jumps[i+j] = res
        #                 print(jumps)
        #                 if (i+j == len(nums) - 1):
        #                     return res


        return jumps[-1]
                

            
            