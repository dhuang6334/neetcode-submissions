class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        prodMax = 1
        prodMin = 1

        for n in nums:
            if n == 0:
                prodMax = prodMin = 1

            temp = prodMax
            prodMax = max(n*prodMax, n*prodMin, n)
            prodMin = min(n*temp, n*prodMin, n)
            res = max(prodMax, res)
            print(res)
            print(prodMax)
            print(prodMin)

        return res