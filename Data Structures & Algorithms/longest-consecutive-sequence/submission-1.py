class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        group = set(nums)

        check = []
        longest = 0
        for num in nums:
            # if (num + 1) in group:
            #     if (num - 1) not in group:
            #         chains[num] = 1
            #     else:
            #         chains[num - longest - 1] += 1
            #         if chains[num - longest - 1] > longest:
            #             longest = chains[num - longest - 1]

            if (num - 1) not in group:
                check.append(num)
        
        for num in check:
            count = 1
            while (num + 1) in group:
                count += 1
                num += 1
            
            if (count > longest):
                longest = count

        print(check)
        return longest
             