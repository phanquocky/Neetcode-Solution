from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(k):
      res.append(freq[i][0])

    return res

sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))