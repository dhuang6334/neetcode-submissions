class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prodLeft = []

        prod = 1

        for i in range(len(nums)):
            prodLeft.append(prod)
            prod *= nums[i]

        prodRight = [0] * len(nums)

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prodRight[i] = prod
            prod *= nums[i]

        output = []

        for i in range(len(nums)):
            output.append(prodLeft[i] * prodRight[i])

        return output
