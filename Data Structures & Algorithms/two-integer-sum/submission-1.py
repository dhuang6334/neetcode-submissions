class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in check.keys():
                return [check[complement], i]
            else:
                check[nums[i]] = i

        return []
