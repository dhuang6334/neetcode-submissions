class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)

        if (size1 > size2):
            return False

        count = [0] * 26

        for char in s1:
            count[ord(char) - ord('a')] += 1

        count2 = [0] * 26
        for i, char in enumerate(s2):
            count2[ord(char) - ord('a')] += 1
            if (i > size1 - 1):
                count2[ord(s2[i - size1]) - ord('a')] -= 1
            if (count == count2):
                return True
            print(count)
            print(count2)
            # if count[ord(char) - ord('a')] == 0:
            #     continue
            # elif count2[ord(char) - ord('a')] + 1 > count[ord(char) - ord('a')]:
            #     continue
            # else:
            #     count2[ord(char) - ord('a')] += 1
            #     if (count == count2):
            #         return True

        return False
