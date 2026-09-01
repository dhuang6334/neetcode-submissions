class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = defaultdict(bool)
        for num in nums:
            if vals[num] == True: 
                return True
            vals[num] = True
        return False