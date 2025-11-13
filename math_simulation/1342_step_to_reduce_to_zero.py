from typing import List #🛑(automatic)
class Solution:
    def numberOfSteps(self,num:int) -> int:
        i = 0
        while num !=0:
            if num % 2 == 0:
                num = num/2
                i = i+1
            else:
                num = num-1
                i = i+1
        return i

num = 14#🛑
answer = Solution()#🛑

for x in range(3):#🛑
    printout = answer.numberOfSteps(num)#🛑
    print(printout)#🛑
    if num == 14:#🛑
        num = 8#🛑
    elif num == 8:#🛑
        num = 123#🛑




