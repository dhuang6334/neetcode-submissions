class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lowers, uppers, lowert, uppert = [0] * 26, [0] * 26, [0] * 26, [0] * 26

        for char in t:
            if char.islower():
                lowert[ord(char) - ord('a')] += 1
            else:
                uppert[ord(char) - ord('A')] += 1

        best = (0, 2000)
        # found = True
        i, j = 0, 0
        size = len(s)

        def contains(upper, lower, char):
            if char.islower() and lower[ord(char) - ord('a')] > 0:
                return True
            elif char.isupper() and upper[ord(char) - ord('A')] > 0:
                return True
            else:
                return False

        def compare(counts, countt):
            for i, count in enumerate(counts):
                if (count < countt[i]):
                    return False
            return True

        while i < size or j < size:

            if not contains(uppert, lowert, s[i]):
                
                # else:
                    # print("DNE")
                # print("NEXT")
                # print(lowers)
                # print(uppers)
                
                # print("NEXT")
                print("IF one " + str(i) + " " + str(j))
                i += 1
                if (i > j):
                    j = i
                
                
            elif j >= size:
                # increment i do check
                # print(uppert)
                # print(uppers)
                # print(lowers == lowert and uppers == uppert)
                if compare(lowers, lowert) and compare(uppers, uppert):
                    if (j - i < best[1] - best[0]):
                        print("elif Best" + str(i) + " " + str(j))
                        best = (i, j)  
                    
                if s[i].islower() and lowert[ord(s[i]) - ord('a')] > 0:
                    lowers[ord(s[i]) - ord('a')] -= 1
                elif s[i].isupper() and uppert[ord(s[i]) - ord('A')] > 0:
                    uppers[ord(s[i]) - ord('A')] -= 1
                else:
                    print("Error subtract")
                print("elif j >=size " + str(i) + " " + str(j))
                i += 1
                # print("NEXT")
                # print(lowers)
                # print(uppers)
                
                # print("NEXT")
                
            else:
                if s[j].islower() and lowert[ord(s[j]) - ord('a')] > 0:
                    lowers[ord(s[j]) - ord('a')] += 1
                elif s[j].isupper() and uppert[ord(s[j]) - ord('A')] > 0:
                    uppers[ord(s[j]) - ord('A')] += 1
                print("else " +  str(i) + " " + str(j))

                # print(uppert)
                print(uppers)
                # print(lowers == lowert and uppers == uppert)
                if compare(lowers, lowert) and compare(uppers, uppert):
                    if (j + 1 - i < best[1] - best[0]):
                        print("else Best" + str(i) + " " + str(j))
                        best = (i, j + 1)  
                    
                    if s[i].islower() and lowert[ord(s[i]) - ord('a')] > 0:
                        lowers[ord(s[i]) - ord('a')] -= 1
                    elif s[i].isupper() and uppert[ord(s[i]) - ord('A')] > 0:
                        uppers[ord(s[i]) - ord('A')] -= 1
                    else:
                        print("Error subtract")
                    i += 1
                # print("NEXT")
                # print(lowers)
                # print(uppers)
               
                # print("NEXT")
                j += 1
                
            

        
        # for j, char in enumerate(s):
        #     if (char.islower() and lowert[ord(char) - ord('a')] > 0):
        #         found = False
        #         lowers[ord(char) - 'a'] += 1
        #         if lowers == lowert and uppers == uppert:
        #             print(lowers)
        #             print(uppers)
        #             print(str(i) + " " + str(j))
        #             found = True
        #             if (j - i < best[1] - 1 - best[0]):
        #                 best = (i, j + 1)
        #     elif char.isupper() and uppert[ord(char) - ord('A')] > 0:
        #         found = False
        #         uppers[ord(char) - ord('A')] += 1
        #         if lowers == lowert and uppers == uppert:
        #             print(lowers)
        #             print(uppers)
        #             print(str(i) + " " + str(j))
        #             found = True
        #             if (j - i < best[1] - 1 - best[0]):
        #                 best = (i, j + 1)
        #     elif found:
        #         if (s[i].islower() and lowert[ord(s[i]) - ord('a')] > 0):
        #             lowers[ord(s[i]) - 'a'] -= 1
        #             i += 1
        #             while (lowert[ord(s[i]) - ord('a')] == 0 if s[i].islower() else uppert[ord(s[i]) - ord('A')] == 0):
        #                 i += 1
        #             found = False
        #         elif s[i].isupper() and uppert[ord(s[i]) - ord('A')] > 0:
        #             uppers[ord(s[i]) - ord('A')] -= 1
        #             i += 1
        #             while (lowert[ord(s[i]) - ord('a')] == 0 if s[i].islower() else uppert[ord(s[i]) - ord('A')] == 0):
        #                 i += 1
        #             found = False
        #         else:
        #             print("ERROR")
        #             print(lowers)
        #             print(uppers)
        #             print(str(i) + " " + str(j))
        #             print("ERROR")
        #         print("NEXT")
        #         print(lowers)
        #         print(uppers)
        #         print(str(i) + " " + str(j))
        #         print("NEXT")
                

        if (best[1] == 2000):
            return ""
        return s[best[0]: best[1]]