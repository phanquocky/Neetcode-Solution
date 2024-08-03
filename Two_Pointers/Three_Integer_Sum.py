from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-2):
      if (i > 0) and nums[i- 1] == nums[i]:
        continue
      left = i + 1
      right = n-1
      while (left < right):
        target = nums[i] + nums[left] + nums[right]
        if target == 0:
          res.append([nums[i], nums[left], nums[right]])
          left += 1
          while(left < n and nums[left ] == nums[left- 1]):
            left += 1
          right -= 1
        elif target < 0:
          left += 1
        else:
          right -= 1
    # print("sorted nums: ", nums)
    return res

sol = Solution()
print(sol.threeSum([0,0,0]))
