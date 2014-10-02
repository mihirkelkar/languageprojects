def check_if_subtree(tree_s, tree_t):
  #Assume that we have the in_order and pre-order functions implemented as a part of the base_class
  if ''.join(tree_s.in_order()) in ''.join(tree_t.in_order()):
    if ''.join(tree_s.pre_order()) in ''.join(tree_t.pre_order()):
      return True
  return False
