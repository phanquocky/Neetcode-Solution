from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      l = len(nums)
      productLeft = [1]
      tem = 1
      for i in range(l):
        tem = tem * nums[i]
        productLeft.append(tem)
      
      productRight = [1]
      tem = 1
      for i in range(l-1, -1, -1):
        tem = tem * nums[i]
        productRight.append(tem)
      
      res = []
      for i in range(l):
        res.append(productLeft[i] * productRight[l - (i + 1)])
        
      return res
  
sol = Solution()
print(sol.productExceptSelf([1,2,4,6])) # [48, 24, 12, 8]

# productLeft = 1 1 2 8 48
# productRight = 1 6 24 48 48