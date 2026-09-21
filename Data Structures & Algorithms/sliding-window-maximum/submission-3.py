from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        bst = SortedList([])

        r = 0
        out = []
        while r < len(nums):
            bst.add(nums[r])
            if len(bst) > k:
                bst.remove(nums[r - k])
            if len(bst) == k:
                out.append(bst[-1])
            
            # print(bst)
            r += 1
        return out
