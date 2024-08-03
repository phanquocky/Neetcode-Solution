from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    res = 0

    while left < right:
      while left < len(height) and height[left] == 0:
        left += 1
      while right >= 0 and  height[right] == 0:
        right -= 1
      
      for i  in range(left, right+1):
        if height[i] == 0:
          res += 1
        else:
          height[i] -= 1
        
    return res
  
sol = Solution()
print(sol.trap([0,2,0,3,1,0,1,3,2,1]))