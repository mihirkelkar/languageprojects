class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
def level_order(root):
  if root == None:
    return root
  queue = [root]
  current , nextcount = 1, 0
  while queue:
    current_node = queue.pop(0)
    print current_node.value
    current -= 1
    if current_node.left != None:
      queue.append(current_node.left)
      nextcount += 1
    if current_node.right != None:
      queue.append(current_node.right)
      nextcount += 1
    if current == 0:
      print "\n"
      current, nextcount = nextcount, current

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
  level_order(root)

if __name__ == "__main__":
  main()
