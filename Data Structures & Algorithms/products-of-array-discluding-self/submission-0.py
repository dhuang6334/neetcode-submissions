class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        left = [0] * size
        right = [0] * size
        for i in range(size):
            left[i] = left[i-1] * nums[i-1] if (i > 1) else nums[0] if (i == 1) else 1
            right[size - i - 1] = right[size - i] * nums[size - i] if (i > 1) else nums[size - 1] if (i==1)  else 1
        
        out = []
        for i in range(size):
            out.append(left[i]*right[i])

        print(left)
        print(right)
        return out

        # prod = 1

        # for num in nums:
        #     prod *= num
        
        

        # def divide(a: int, b: int) -> int:
        #     log = int(math.log(a, 2))
        #     total = a
        #     out = 0
        #     for power in range(log, -1, -1):
        #         diff = b << power
        #         if not (total - diff < 0):
        #             total -= diff
        #             out += 2**power
        #             if total < b:
        #                 return out
        #     return out

        # res = []

        # for num in nums:
        #     if num = 
        #     res.append(divide(prod, num))
        
        # print(divide(100, 7))
        # return res