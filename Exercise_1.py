class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file

  """
  Time Complexity: O(n)
  Space Complexity: O(n)
  """


  def __init__(self):
      self.items = []
         
  def isEmpty(self):
      return True if len(self.items) == 0 else False
         
  def push(self, item):
      self.items.append(item)
         
  def pop(self):
      if self.isEmpty():
          return -1
      return self.items.pop()
        
  def peek(self):
      if self.isEmpty():
          return -1
      return self.items[-1]
        
  def size(self):
      return len(self.items)
         
  def show(self):
      return self.items
          
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
