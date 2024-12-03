class MinStack(object):
  stack = []
  def __init__(self):
    pass

  def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    m = 0
    if (len(self.stack) > 0):
      m = min(val, self.getMin())
    else:
      m = val
    self.stack.append([val, m])  

  def pop(self):
    """
    :rtype: None
    """
    self.stack.pop()

  def top(self):
    """
    :rtype: int
    """
    if len(self.stack) > 0:
      return self.stack[len(self.stack) - 1][0]
      

  def getMin(self):
    """
    :rtype: int
    """
    if len(self.stack) > 0:
      return self.stack[len(self.stack) - 1][1]
      


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-1))
print(obj.push(3))
print(obj.push(-4))
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.top())