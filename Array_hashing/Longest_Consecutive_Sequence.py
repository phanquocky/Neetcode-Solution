from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		s  = set(nums)
		res = 0
		
		for n in nums:
			if n - 1 in s:
				continue
			else:
				length = 1
				while (length + n ) in s:
					length += 1
				res = max(res, length)
		return res
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
