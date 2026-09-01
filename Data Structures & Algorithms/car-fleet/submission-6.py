class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joint = zip(position, speed)
        joint = sorted(joint, key=lambda x: x[0], reverse=True)
        
        stack = []
        for p, s in joint:
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        # def compare(posA, spdA, posB, spdB, targ):
        #     if spdA > spdB:
        #         calc = (posB - posA)/(spdA - spdB) * spdA + posA
        #         if ( calc <= target and calc > max(posA, posB)):
        #             return True
        #     return False
        
        # fleets = 1

        # for i in range(len(joint)):
        #     if (i < len(joint) - 1):
        #         if (not compare(joint[i][0], joint[i][1], joint[i+1][0], joint[i+1][1], target)):
        #             fleets +=1
        
        # time = []

        # for i in range(len(position)):
        #     #calc = (joint[i+1][0] - joint[i][0])/ (joint[i][1] - joint[i+1][1])
        #     if (i < len(position) - 1 and ((joint[i][1] > joint[i+1][1])) and ((joint[i+1][0] - joint[i][0])/ (joint[i][1] - joint[i+1][1]))< target and (joint[i+1][0] - joint[i][0])/ (joint[i][1] - joint[i+1][1]) > max(joint[i][0], joint[i+1][0])):
        #         time.append(0) #(target - joint[i+1][0])/joint[i+1][1])
        #     else:
        #         time.append((target - joint[i][0])/joint[i][1])
        
        # print(time)
        # for i in range(len(time) - 1, -1, -1):
        #     if i > 0 and time[i - 1] == 0:
        #         time[i - 1] = time[i] 

        # print(time)
        # time = sorted(time)

        # fleets = 1

        # for i in range(len(time)):
        #     if (i > 0 and abs(time[i] - time[i-1]) > 0.0001):
        #         fleets += 1
        
        # return fleets
