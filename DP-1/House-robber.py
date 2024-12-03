from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n + 7)
    dp[1] = nums[0]

    for i in range (2, n + 1):
      dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    return dp[n]
  
  
sol = Solution()
print(sol.rob([2,7,9,3,1]))


a = "abcaa"
a.split("")

print(a.split())