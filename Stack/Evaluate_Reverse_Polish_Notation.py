class Solution(object):
  def isOperation(self, op):
    return op == "+" or op == "-" or op == "*" or op == "/"
  def calc(self, y, x, op):
    if op == "+" :
      return y + x
    if op == "-" :
      return y - x
    if op == "*":
      return y * x
    if op == "/":
      return int(y / x)

  def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
      if self.isOperation(token):
        x = stack.pop()
        y = stack.pop()

        stack.append(self.calc(y, x, token))
      else:
        stack.append(int(token))
    
    return stack.pop()
  
sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    