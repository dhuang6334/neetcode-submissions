class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        j = len(numbers)

        while (i < j):
            total = numbers[i-1] + numbers[j-1]
            if (total == target):
                return [i, j]
            elif (total > target):
                j -=1
            else:
                i +=1