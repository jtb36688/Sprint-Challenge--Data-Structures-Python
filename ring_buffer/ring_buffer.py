class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None]*capacity

  def append(self, item):
    print("running append")
    del self.storage[-1]
    self.storage.insert(0, item)




  def get(self):
    orderedlist = [None]*self.capacity
    for i in range(len(self.storage)-1):
      del orderedlist[-1]
      orderedlist.insert(0, self.storage[i])
    checked = False
    while not checked:
      if orderedlist[-1] == None:
        del orderedlist[-1]
      else:
        checked = True
    return orderedlist