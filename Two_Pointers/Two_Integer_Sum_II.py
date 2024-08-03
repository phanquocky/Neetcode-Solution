from typing import List
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1

    while (left < right):
      t = numbers[left] + numbers[right]
      if t == target:
        return [left + 1, right + 1]
      elif t < target:
        left += 1
      else:
        right -= 1
    return []
  
sol = Solution()
print(sol.twoSum([1,2,3,4], 3))