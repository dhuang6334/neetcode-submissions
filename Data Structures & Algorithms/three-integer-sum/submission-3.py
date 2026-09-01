class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        sort = sorted(nums)
        size = len(nums)
        

        for j in range(size):
            i = 0
            k = size - 1
            while (i < k):
                if (i == j):
                    i += 1
                    continue
                elif (j == k):
                    k -= 1
                    continue
                total = sort[i] + sort[j] + sort[k]
                if total == 0:
                    if (j > i) and (j < k):
                        out.add((sort[i], sort[j], sort[k]))
                    elif (j >= k):
                        out.add((sort[i], sort[k], sort[j]))
                    else:
                        out.add((sort[j], sort[i], sort[k]))
                    i += 1
                    k -= 1
                elif (total < 0):
                    i += 1
                else:
                    k -= 1
                
                # print(str(i) + "," + str(j) + "," + str(k))
        
        
        print(out)
        print(sort)
        return [list(t) for t in out]