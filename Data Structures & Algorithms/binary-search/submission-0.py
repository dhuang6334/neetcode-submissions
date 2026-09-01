class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(_nums: List[int], a, b, targ):
            if (a > b):
                return -1
            mid = (a + b)//2
            if _nums[mid] == targ:
                return mid
            elif _nums[mid] > targ:
                return helper(_nums, a, mid - 1, targ)
            else: 
                return helper(_nums, mid + 1, b, targ)
        return helper(nums, 0, len(nums) - 1, target)