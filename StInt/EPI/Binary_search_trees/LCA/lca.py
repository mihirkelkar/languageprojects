def least_common_ancestor(val_a, val_b, tree.root):
  flag = True:
  lca = tree.root
  while flag:
    if val_a == lca.value or val_b == lac.value:
      return lca
    elif (val_a > lca.value and val_b < lca.value) or (val_a < lca.value and val_b > lca.value):
      return lca
    elif val_a < lca.value and val_b < lca.value:
      temp = lca.left
    elif val_a > lca.value and val_b > lca.value:
      temp = lca.right
    if temp != None:
      lca = temp
    else:
      return None
