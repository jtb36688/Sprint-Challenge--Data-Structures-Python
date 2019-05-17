class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None]*capacity

  def append(self, item):
    print("running append")
    if len(self.storage) == self.capacity:
      self.storage[-1] = None
      self.storage[0] = item
    else:
      self.storage[0] = item



  def get(self):
    orderedlist = [None]*self.capacity
    for i in range(len(self.storage)-1):
      orderedlist.insert(0, self.storage[i+1])
    return orderedlist