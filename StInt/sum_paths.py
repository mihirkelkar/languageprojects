class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
 
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.right = Node(4)


def calculate_path_sum(node, sum_so_far = 0, final_sum = 0):
  sum_so_far = sum_so_far * 10 + node.value
  if node.left == None and node.right == None:
    final_sum += sum_so_far
  else:
    if node.left != None:
      final_sum = calculate_path_sum(node.left, sum_so_far, final_sum)
    if node.right != None:
      final_sum = calculate_path_sum(node.right, sum_so_far, final_sum)
  return final_sum
  
print calculate_path_sum(root)
