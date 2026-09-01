class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for char in s:
            if char.isalnum():
                newString += char.lower()

        size = len(newString)
        print(newString)
        for i in range(size):
            if newString[i] != newString[size - i - 1]:
                return False
        return True