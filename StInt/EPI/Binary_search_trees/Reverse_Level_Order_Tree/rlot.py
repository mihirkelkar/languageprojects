class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def reverse(root):
  if root == None:
    return None
  queue = [root]
  current_count = 1
  next_count = 0
  depth_track = [1]
  nodes = []
  while queue:
    cnode = queue.pop(0)
    nodes.append(cnode)
    current_count -= 1
    if cnode.left != None:
      queue.append(cnode.left)
      next_count += 1
    if cnode.right != None:
      queue.append(cnode.right)
      next_count += 1
    if current_count == 0:
      current_count , next_count = next_count, current_count
      if current_count != 0:
        depth_track.append(current_count)
  for ii in reversed(depth_track):
    while ii != 0:
      print nodes.pop().value,
      ii -= 1
    print "\n"

def main():
  root = Node(1) 
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
  reverse(root)

if __name__ == "__main__":
  main()
