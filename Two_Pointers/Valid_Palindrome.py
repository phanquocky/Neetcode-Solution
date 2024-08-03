class Solution:
  def isalphanumerical(self, a: str) -> str:
    
    if  ("a" <= a and a <= "z") or ("A" <= a and a <= "Z") or ("0" <= a and a <= "9"):
      return a.lower()
    return ""

  def isPalindrome(self, s: str) -> bool:
    tem = ""
    for i in s:
      tem += self.isalphanumerical(i)

    print(tem)

    left = 0
    right = len(tem) - 1

    while (left <= right):
      
      if tem[left] != tem[right]:
        return False
      left += 1
      right -= 1
    
    return True
  
sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?")) # True