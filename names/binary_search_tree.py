class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.value > target:
      if not self.left:
        return False
      return self.left.contains(target)
    else:
      if not self.right:
        return False
      return self.right.contains(target)

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
  def for_each(self, cb):
    self.value = cb(self.value)
    if self.right:
      self.right.for_each(cb)
    if self.left:
      self.left.for_each(cb)