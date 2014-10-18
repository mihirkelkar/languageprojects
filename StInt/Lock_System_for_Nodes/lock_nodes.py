class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.locked = False

  def isLocked(self):
    return self.locked
  
  def setLock(self):
    self.locked = True

  def unlock(self):
    self.locked = False

class BTree(object):
  def __init__(self):
    self.head = None

  def add_node(self, value, root = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left != None:
          self.add_node(value, root.left)
        else:
          root.left = Node(value)
      elif value > root.value:
        if root.right != None:
          self.add_node(value, root.right)
        else:
          root.right = Node(value)

  def child_check(self, root):
    if root != None:
      if root.locked:
        return True
      if root.left != None:
        l = self.child_check(root.left)
      if root.right != None:
        r = self.child_check(root.right)
      return r and l
    else:
      return False
      
  def lock(self, value, root = self.root):
    root = self.root if root is None else root
    if value < root.value and !root.isLocked():
      if root.left != None:
        self.lock(value, root.left)

    elif value > root.value and !root.isLocked():
      if root.right != None:
        self.lock(value, root.right)

    elif value == root.value:
      if !self.child_check(root):
        root.setLock()
        print "Lock Set"
      
  #unlock is essentially just search and unlock
  
  def unlock(self, value, root = self.root):
    root = self.root if root is None else root
    if value < root.value:
      if root.left != None:
        self.unlock(self, value, root.left)
    elif value > root.value:
      if root.right != None:
        self.unlock(self, value, root.right)
    elif value == root.value:
      root.unlock()
