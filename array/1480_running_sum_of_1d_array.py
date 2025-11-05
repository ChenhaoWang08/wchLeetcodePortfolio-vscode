
#Not included in leetcode prgramming space = 🛑
from typing import List #🛑(automatic)
nums = [1,2,3,4]#Included in leetcode example
'Output should be [1,3,6,10]'

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):# a loop for the bottom summation to repeat through thr list
            nums[i] += nums[i - 1] #tHe math summatioon in sequence
        return nums #after summation, gives out the output
    

solution = Solution()#🛑
output = solution.runningSum(nums)#🛑 line 14-15 set up executing output

print(output)#🛑 printing output
