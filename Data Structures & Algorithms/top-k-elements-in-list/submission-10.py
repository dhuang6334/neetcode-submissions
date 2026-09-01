class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
    
        for num in nums:
            count[num] += 1
        

        size = len(nums)
        buckets = [[] for _ in range(size)]
        
        for num, cnt in count.items():
            # if (buckets[cnt - 1] != 0):
            #     unique = list(count.keys())
            #     left = size - len(unique)
            #     buckets = ([0] * left) + unique
            #     break 
            buckets[cnt - 1].append(num)

        
        out = []
        for i in range(size - 1, -1, -1):
            print(buckets[i])
            for num in buckets[i]:
                if num != None:
                    out.append(num)
                    k -= 1
                if k <= 0:
                    print(buckets)
                    print(count)
                    return out
        
        return out
