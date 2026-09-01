class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort idea!!

        freq = [[] for _ in range(len(nums) + 1)]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count.keys():
            freq[count[num]].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

        return []