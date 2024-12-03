class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    m = {}
    for char in s:
      if char in m:
        m[char] += 1
      else:
        m[char] = 1
    for char in t:
      if char in m:
        m[char] -= 1
      else:
        return False
    
    for key,val in m.items():
      if val != 0:
        return False
    return True