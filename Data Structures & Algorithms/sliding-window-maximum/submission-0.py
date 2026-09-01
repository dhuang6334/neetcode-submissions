from heapq import heapify, heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
   
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
        
        global size
        size = 0
        # def siftUp(heap: List[int], i: int) -> List[int]:
        #     if ((i - 1)//2 < 0):
        #         return heap
        #     elif (heap[(i-1)//2] > heap[i]):
        #         return heap
        #     else:
        #         temp = heap[i]
        #         heap[i] = heap[(i-1)//2]
        #         heap[(i-1)//2] = temp
        #         return siftUp(heap, (i-1)//2)
        # def siftDown(heap: List[int], i: int) -> List[int]:
        #     if (i >= size//2):
        #         return heap
        #     elif (heap[i] > heap[2*i + 1] and heap[i] > heap[2*i + 2]):
        #         return heap
        #     elif (heap[2*i + 2] < heap[2*i + 1]):
        #         temp = heap[i]
        #         heap[i] = heap[2*i + 1]
        #         heap[2*i + 1] = temp
        #         return siftDown(heap, 2*i + 1)
        #     elif (heap[2*i + 1] < heap[2*i + 2]):
        #         temp = heap[i]
        #         heap[i] = heap[2*i + 2]
        #         heap[2*i + 2] = temp
        #         return siftDown(heap, 2*i + 2)
        #     else:
        #         print("ERROR")
        #         return []


        # def heappush(heap: List[int], n: int) -> List[int]:
            
        #     size += (1 if (size < k) else 0)
        #     heap[size-1] = n
        #     return siftUp(heap, size-1)
        
        # def heappop(heap: List[int]) -> int:
            
        #     if size == 0:
        #         raise IndexError()
        #     temp = heap[0]
        #     heap[0] = heap[size-1]
        #     size -= 1
        #     # heap[k-1] = temp Popped off
        #     siftDown(heap, 0)

        #     return temp

        out = []
        heap = []
        for i, num in enumerate(nums):
            
            if i >= k - 1:
                out.append(heappushpop(heap, num))
            else:
                heappush(heap, num)

        return out

