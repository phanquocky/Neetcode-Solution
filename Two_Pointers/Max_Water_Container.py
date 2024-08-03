from typing import List

class Solution:
  def maxArea(self, heights: List[int]) -> int:
    res = 0
    left = 0
    right = len(heights) - 1

    while (left < right):
      area = min(heights[left], heights[right]) * (right - left)
      res = max(res, area)

      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1

    return res

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))