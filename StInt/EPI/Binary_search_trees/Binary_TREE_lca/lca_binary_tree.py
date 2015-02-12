
def binary_tree_common_ancestor(val_a, val_b, root):
  if root == None:
    return  False
  elif root.value == val_a or root.value == val_b:
    return True
  else:
    left_answer = binary_tree_lca(root.left)
    right_answer = binary_tree_lca(root.right)
    if left_answer and right_answer:
      final_root = root
      return True
