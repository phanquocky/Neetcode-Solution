class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    mm = {
      "{": "}",
      "[": "]",
      "(": ")" 
    }
    for a in s:
      if a == "(" or a == "{" or a == "[":
        stack.append(a)
      else:
        if len(stack) ==0:
          return False
        tem = stack.pop()
        if mm[tem] != a:
          return False
    return len(stack) == 0
  
sol = Solution()
print(sol.isValid("()")) # True