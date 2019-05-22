class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if not self.storage[0] == None:
      self.storage[self.current] = item
      if self.current < self.capacity-1:
        self.current += 1
      else:
        self.current = 0
    else:
      del self.storage[0]
      self.storage.append(item)

  def get(self):
    orderedlist = [None]*self.capacity
    for i in range(len(self.storage)):
      del orderedlist[-1]
      orderedlist.insert(0, self.storage[i])
    orderedlist.reverse()
    checked = False
    while not checked:
      if orderedlist[-1] == None:
        del orderedlist[-1]
      elif orderedlist[0] == None:
        del orderedlist[0]
      else:
        checked = True
    return orderedlist