from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque([])

        r = 0
        out = []
        while r < len(nums):
            
            
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)
            if deq[0] < r - k + 1:
                deq.popleft()
            if r >= k - 1:
                out.append(nums[deq[0]])
            
            # print(deq)
            r += 1
        return out
