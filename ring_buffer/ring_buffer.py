class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if None in self.storage:
      self.storage[self.storage.index(None)] = item
      self.current += 1
    else:
      if self.current == self.capacity:
        self.current = 0
      self.storage[self.current] = item
      self.current += 1

  def get(self):
  #returning values only when it is not null
    return [value for value in self.storage if value is not None]